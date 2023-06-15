# -*- coding: utf-8 -*-

# -- Sheet --

!pip install snowflake-connector-python
!pip install tldextract
!pip install py2neo

import requests
import pandas as pd
import numpy as np
import snowflake.connector
import os
from py2neo import Graph
from py2neo.bulk import merge_nodes, create_relationships, merge_relationships
from urllib.parse import urlparse

#[Environment Configs]
client_id = "d0afa05e7ab642acb0497f018b601b86"
client_secret = "ikdU3eOtXRmMR9oWlEnP0W0jAVZYNMBF2FUwsuwtHkZ37Oh4IZZkso3tFdsbfdmO"  
os.environ["HTTP_PROXY"] = "http://d161560-001.dc.gs.com:8899"
os.environ["HTTPS_PROXY"] = "http://d161560-001.dc.gs.com:8899"

#[Credentials]
host = "xplore.graph-x.site.gs.com"
port = "7687"
username = "neo4j"
password = "xplorer"
graph = Graph(host=host, port=port, auth=(username, password))
BATCHES = 100

# ### Libraries & Shared Code


def get_oauth_tokens(client_id: str, client_secret: str):
    _IDFS_URL = "https://idfs.gs.com/as/token.oauth2"
    response = requests.post(
        url = _IDFS_URL,
        params = {"access_token_manager_id": "JwtSnowflake"},  # This must be set to JwtSnowflake to generate Snowflake-compatible OAuth Token
        data = {"grant_type": "client_credentials", "scope": "SESSION:ROLE-ANY"},
        auth = (client_id, client_secret),
    )
    response = response.json()
    if "access_token" not in response.keys():
        raise PermissionError(f"Not authorized to access OAuth Tokens: {response}")
    return response["access_token"]
  
def connect_snowflake(user: str, database: str, token: str) -> snowflake.connector.cursor:
    """Connect to Snowflake and return an authorized cursor. Below uses Catalyst connections
   
    :param user: Client ID from OAuth2 Authentication
    :param database: Name of database to connect to
    :param token: Generated OAuth Token. Please either generate and save to a tmp file in a separate thread OR use subprocess module to call the underlying subsystem and capture the output
    :return: Snowflake Cursor
    """
    snow_connector = snowflake.connector.connect(
        user=user,
        authenticator="oauth",
        account="sfamdprvtawseast1d01.goldman.us-east-1.aws.privatelink",
        role="AMD_CATALYST_DATA_RW",
        warehouse="AMD_CATALYST_RW",
        database=database,
        ocsp_fail_open=False,
        token=token,
    )
    cursor = snow_connector.cursor()
    return cursor
 
def disconnect(cursor: snowflake.connector.cursor) -> None:
    try:
        cursor.close()
    except:
        raise Exception("Failed to close cursor")   
        
oauth_token = get_oauth_tokens(client_id, client_secret)
cursor = connect_snowflake(client_id, "AMD_CATALYST_DB", oauth_token)

# ### SourceScrub


sourcescrub_organizations_df = cursor.execute('SELECT ID, NAME, DOMAIN, LINKEDIN, TWITTER, FACEBOOK, CRUNCHBASE, FOUNDINGYEAR, CITY, STATE, COUNTRY, SPECIALTIES, TOTALAMOUNTINVESTED FROM L1.SOURCESCRUB_COMPANY WHERE DOMAIN IS NOT NULL OR LINKEDIN IS NOT NULL OR TWITTER IS NOT NULL OR FACEBOOK IS NOT NULL OR CRUNCHBASE IS NOT NULL').fetch_pandas_all()
display(sourcescrub_organizations_df.head(10))

sourcescrub_organizations_df.rename(columns={'ID': 'SOURCE_ID', 'FOUNDINGYEAR': 'TIME_OF_FOUNDING', 'TOTALAMOUNTINVESTED': 'TOTAL_AMOUNT_INVESTED'}, inplace=True)
sourcescrub_organizations_df['SOURCE_ID'] = sourcescrub_organizations_df['SOURCE_ID'].astype(str)
sourcescrub_organizations_df['TIME_OF_FOUNDING'] = sourcescrub_organizations_df['TIME_OF_FOUNDING'].fillna(0).astype('int').replace(0, np.nan)
sourcescrub_organizations_df['SOURCE_ID'] = 'sourcescrub-' + sourcescrub_organizations_df['SOURCE_ID']

sourcescrub_organizations_df['LINKEDIN'] = sourcescrub_organizations_df['LINKEDIN'].apply(lambda x: (str(urlparse(x).netloc or '') + str(urlparse(x).path or '')).lstrip('www.'))
sourcescrub_organizations_df['TWITTER'] = sourcescrub_organizations_df['TWITTER'].apply(lambda x: (str(urlparse(x).netloc or '') + str(urlparse(x).path or '')).lstrip('www.'))
sourcescrub_organizations_df['FACEBOOK'] = sourcescrub_organizations_df['FACEBOOK'].apply(lambda x: (str(urlparse(x).netloc or '') + str(urlparse(x).path or '')).lstrip('www.'))
sourcescrub_organizations_df['CRUNCHBASE'] = sourcescrub_organizations_df['CRUNCHBASE'].apply(lambda x: (str(urlparse(x).netloc or '') + str(urlparse(x).path or '')).lstrip('www.'))

sourcescrub_organizations_df.replace(r'^\s*$', np.nan, regex=True, inplace=True)

sourcescrub_organizations_df.head()

# ### Ingesting Common SourceScrub Identifiers into Graph


sourcescrub_organizations_df_website = np.array_split(sourcescrub_organizations_df[sourcescrub_organizations_df['DOMAIN'].isna() == False][['DOMAIN']].rename(columns={'DOMAIN': 'URL'}).to_dict('records'), BATCHES)
for chunk_df in sourcescrub_organizations_df_website:
    merge_nodes(
        graph.auto(),
        chunk_df,
        (("URLIdentifier", "DomainURL"), "URL"),
    )

sourcescrub_organizations_df_linkedin = np.array_split(sourcescrub_organizations_df[sourcescrub_organizations_df['LINKEDIN'].isna() == False][['LINKEDIN']].rename(columns={'LINKEDIN': 'URL'}).to_dict('records'), BATCHES)
for chunk_df in sourcescrub_organizations_df_linkedin:
    merge_nodes(
        graph.auto(),
        chunk_df,
        (("URLIdentifier", "LinkedInURL"), "URL"),
    )
    
sourcescrub_organizations_df_twitter = np.array_split(sourcescrub_organizations_df[sourcescrub_organizations_df['TWITTER'].isna() == False][['TWITTER']].rename(columns={'TWITTER': 'URL'}).to_dict('records'), BATCHES)
for chunk_df in sourcescrub_organizations_df_twitter:
    merge_nodes(
        graph.auto(),
        chunk_df,
        (("URLIdentifier", "TwitterURL"), "URL"),
    )

sourcescrub_organizations_df_facebook =  np.array_split(sourcescrub_organizations_df[sourcescrub_organizations_df['FACEBOOK'].isna() == False][['FACEBOOK']].rename(columns={'FACEBOOK': 'URL'}).to_dict('records'), BATCHES)
for chunk_df in sourcescrub_organizations_df_facebook:
    merge_nodes(
        graph.auto(),
        chunk_df,
        (("URLIdentifier", "FacebookURL"), "URL"),
    )

sourcescrub_organizations_df_crunchbase =  np.array_split(sourcescrub_organizations_df[sourcescrub_organizations_df['CRUNCHBASE'].isna() == False][['CRUNCHBASE']].rename(columns={'CRUNCHBASE': 'URL'}).to_dict('records'), BATCHES)
for chunk_df in sourcescrub_organizations_df_crunchbase:
    merge_nodes(
        graph.auto(),
        chunk_df,
        (("URLIdentifier", "CrunchbaseURL"), "URL"),
    )

# ### Ingesting SourceScrub Companies into the Graph


sourcescrub_organizations = np.array_split([{k:v for k, v in x.items() if v == v} for x in sourcescrub_organizations_df.to_dict('records')], BATCHES)
for chunk_df in sourcescrub_organizations:
    merge_nodes(
        graph.auto(),
        chunk_df,
        (("Company", "SourcescrubCompany"), "SOURCE_ID"),
    )

for identifier in ['DOMAIN', 'LINKEDIN', 'TWITTER', 'FACEBOOK', 'CRUNCHBASE']:
    sourcescrub_identifier_relationships = sourcescrub_organizations_df.loc[sourcescrub_organizations_df[identifier] != np.nan][['SOURCE_ID', identifier]]
    sourcescrub_identifier_relationships.insert(1, 'WEIGHT', [[0.5]] * len(sourcescrub_identifier_relationships))

    df_list = np.array_split(sourcescrub_identifier_relationships, BATCHES)
    for chunk_df in df_list:
        merge_relationships(
            graph.auto(),
            chunk_df.values.tolist(),
            merge_key="LINKED_TO",
            start_node_key=("Company", "SOURCE_ID"),
            end_node_key=("URLIdentifier", "URL"),
            keys=["WEIGHT"],
        )

# ### CrunchBase


crunchbase_organizations_df = cursor.execute('SELECT CRUNCHBASE_ORGANIZATION_UUID, ORGANIZATION_CITY, FACEBOOK_URL, DOMAIN, TWITTER_URL, FUNDING_ROUND_TYPE, FOUNDED_ON, EMPLOYEE_COUNT, CRUNCHBASE_GROUPS, ORGANIZATION_STATE_CODE, ORGANIZATION_NAME, LINKEDIN_URL, ORGANIZATION_COUNTRY_CODE, CRUNCHBASE_URL FROM L2_NEW.CRUNCHBASE_ORGANIZATIONS WHERE DOMAIN IS NOT NULL OR TWITTER_URL IS NOT NULL OR FACEBOOK_URL IS NOT NULL OR LINKEDIN_URL IS NOT NULL OR CRUNCHBASE_URL IS NOT NULL').fetch_pandas_all()
crunchbase_organizations_df.rename(columns={
    'CRUNCHBASE_ORGANIZATION_UUID': 'SOURCE_ID', 
    'TWITTER_URL': 'TWITTER', 
    'FACEBOOK_URL': 'FACEBOOK',
    'LINKEDIN_URL': 'LINKEDIN',
    'CRUNCHBASE_URL': 'CRUNCHBASE', 
    'FOUNDED_ON': 'TIME_OF_FOUNDING',
    'ORGANIZATION_CITY': 'CITY',
    'ORGANIZATION_STATE_CODE': 'STATE',
    'ORGANIZATION_COUNTRY_CODE': 'COUNTRY', 
    'ORGANIZATION_NAME': 'NAME', 
    'LINKEDIN_URL': 'LINKEDIN'
}, inplace=True)

crunchbase_organizations_df.replace({None: ''}, inplace=True)

crunchbase_organizations_df['LINKEDIN'] = crunchbase_organizations_df['LINKEDIN'].apply(lambda x: (str(urlparse(x.replace('[', '').replace(']', '')).netloc or '') + str(urlparse(x.replace('[', '').replace(']', '')).path or '')).lstrip('www.'))
crunchbase_organizations_df['TWITTER'] = crunchbase_organizations_df['TWITTER'].apply(lambda x: (str(urlparse(x).netloc or '') + str(urlparse(x).path or '')).lstrip('www.'))
crunchbase_organizations_df['FACEBOOK'] = crunchbase_organizations_df['FACEBOOK'].apply(lambda x: (str(urlparse(x).netloc or '') + str(urlparse(x).path or '')).lstrip('www.'))
crunchbase_organizations_df['CRUNCHBASE'] = crunchbase_organizations_df['CRUNCHBASE'].apply(lambda x: (str(urlparse(x).netloc or '') + str(urlparse(x).path or '')).lstrip('www.'))

crunchbase_organizations_df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
display(crunchbase_organizations_df.head())

crunchbase_organizations_df_website = np.array_split(crunchbase_organizations_df[crunchbase_organizations_df['DOMAIN'].isna() == False][['DOMAIN']].rename(columns={'DOMAIN': 'URL'}).to_dict('records'), BATCHES)
for chunk_df in crunchbase_organizations_df_website:
    merge_nodes(
        graph.auto(),
        chunk_df,
        (("URLIdentifier", "DomainURL"), "URL"),
    )

crunchbase_organizations_df_linkedin = np.array_split(crunchbase_organizations_df[crunchbase_organizations_df['LINKEDIN'].isna() == False][['LINKEDIN']].rename(columns={'LINKEDIN': 'URL'}).to_dict('records'), BATCHES)
for chunk_df in crunchbase_organizations_df_linkedin:
    merge_nodes(
        graph.auto(),
        chunk_df,
        (("URLIdentifier", "LinkedInURL"), "URL"),
    )
    
crunchbase_organizations_df_twitter = np.array_split(crunchbase_organizations_df[crunchbase_organizations_df['TWITTER'].isna() == False][['TWITTER']].rename(columns={'TWITTER': 'URL'}).to_dict('records'), BATCHES)
for chunk_df in crunchbase_organizations_df_twitter:
    merge_nodes(
        graph.auto(),
        chunk_df,
        (("URLIdentifier", "TwitterURL"), "URL"),
    )

crunchbase_organizations_df_facebook =  np.array_split(crunchbase_organizations_df[crunchbase_organizations_df['FACEBOOK'].isna() == False][['FACEBOOK']].rename(columns={'FACEBOOK': 'URL'}).to_dict('records'), BATCHES)
for chunk_df in crunchbase_organizations_df_facebook:
    merge_nodes(
        graph.auto(),
        chunk_df,
        (("URLIdentifier", "FacebookURL"), "URL"),
    )

crunchbase_organizations_df_crunchbase =  np.array_split(crunchbase_organizations_df[crunchbase_organizations_df['CRUNCHBASE'].isna() == False][['CRUNCHBASE']].rename(columns={'CRUNCHBASE': 'URL'}).to_dict('records'), BATCHES)
for chunk_df in crunchbase_organizations_df_crunchbase:
    merge_nodes(
        graph.auto(),
        chunk_df,
        (("URLIdentifier", "CrunchbaseURL"), "URL"),
    )

crunchbase_organizations = np.array_split([{k:v for k, v in x.items() if v == v} for x in crunchbase_organizations_df.to_dict('records')], BATCHES)
for chunk_df in crunchbase_organizations:
    merge_nodes(
        graph.auto(),
        chunk_df,
        (("Company", "CrunchbaseCompany"), "SOURCE_ID"),
    )

for identifier in ['DOMAIN', 'LINKEDIN', 'TWITTER', 'FACEBOOK', 'CRUNCHBASE']:
    crunchbase_identifier_relationships = crunchbase_organizations_df.loc[crunchbase_organizations_df[identifier] != np.nan][['SOURCE_ID', identifier]]
    crunchbase_identifier_relationships.insert(1, 'WEIGHT', [[0.5]] * len(crunchbase_identifier_relationships))

    df_list = np.array_split(crunchbase_identifier_relationships, BATCHES)
    for chunk_df in df_list:
        merge_relationships(
            graph.auto(),
            chunk_df.values.tolist(),
            merge_key="LINKED_TO",
            start_node_key=("Company", "SOURCE_ID"),
            end_node_key=("URLIdentifier", "URL"),
            keys=["WEIGHT"],
        )

