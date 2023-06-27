from data_model.nodes import NODES
from data_model.relationships import RELATIONSHIPS
from utility.snowflake_master import snowflake_connector
from utility.ut_env import configs
from utility.logger import logger

DATA_TYPE_MAP = {
    "string": str,
    "integer": int,
    "float": float,
}

BATCH_SIZE = 10_000


def get_df_from_snowflake(sql_query):
    snow_connector = snowflake_connector(configs, schema="l2_new")
    df = snow_connector.cursor.execute(sql_query).fetch_pandas_all()
    return df


def save_df_to_csv(df, source=""):
    """
    Save this csv to the NAS
    :param df:
    :param source:
    :return: None. Use "source" to name the csv dump
    """
    return


def get_fields_for_source(source, nodes=NODES, relationships=RELATIONSHIPS):
    """
    :param source:
    :param nodes:
    :param relationships:
    :return: all the fields required from a given source
    """
    return


def execute_cypher_query(query):
    return


def ingest_nodes(node):
    """
    :param node: is a template node from the data model, and not an actual node
    :return:
    """
    return


def ingest_relationships(relationship, add_nodes=False):
    """
    :param relationship: is a template relationship from the data model, and not an actual relationship
    :param add_nodes: when set to True, this function should also ingest the start and end nodes along with the relationship
    thus eliminating the need to ingest relationships after nodes
    :return:
    """
    return


def delete_nodes(key, df=None):
    return



def delete_relationships(key, df=None):
    return


def standardize_url(url, kind=""):
    """
    :param url: uncleaned url, could vary across source
    :param kind: field name, for example: twitter, linkedin, etc
    :return: cleaned url which doesn't vary across source. Remove non informational prefixes and suffixes like https, //, www.
    """
    return


def standardize_city(x):
    """
    :param x:
    :return: cleaned city name which doesn't vary across data source
    """
    return


def standardize_state(x, return_type="code"):
    """
    :param x:
    :param return_type: "code" or "name"
    :return:
    """
    return


def standardize_country(x, return_type="code"):
    """
    :param x:
    :param return_type: "code" or "name"
    :return:
    """
    return
#%%

#%%
