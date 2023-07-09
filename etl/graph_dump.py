import pandas as pd

from etl.utils import (
    get_fields_for_source,
    get_df_from_snowflake,
    save_df_to_csv,
    standardize_url,
    standardize_city,
    standardize_state,
    standardize_country,
    standardize_job_title,
    get_df_for_industry,
    standardize_ss_industry,
    standardize_cb_industry,
    reduce_industry_df
)

source = "cb_acquisition"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_event"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_event_org"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_event_person"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_investor_investment"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_investor_org"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)
df["city"] = df["CITY"].apply(lambda x: standardize_city(x))
df["state"] = df["STATE_CODE"].apply(lambda x: standardize_state(x, return_type="code"))
df["country"] = df["COUNTRY_CODE"].apply(lambda x: standardize_country(x, return_type="code"))
df["TWITTER"] = df["TWITTER"].apply(lambda x: standardize_url(x))
df["LINKEDIN"] = df["LINKEDIN"].apply(lambda x: standardize_url(x))
df["FACEBOOK"] = df["FACEBOOK"].apply(lambda x: standardize_url(x))
df["DOMAIN"] = df["DOMAIN"].apply(lambda x: standardize_url(x))
save_df_to_csv(df, source=source)

source = "cb_investor_person"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)
df["city"] = df["CITY"].apply(lambda x: standardize_city(x))
df["state"] = df["STATE_CODE"].apply(lambda x: standardize_state(x, return_type="code"))
df["country"] = df["COUNTRY_CODE"].apply(lambda x: standardize_country(x, return_type="code"))
df["TWITTER"] = df["TWITTER"].apply(lambda x: standardize_url(x))
df["LINKEDIN"] = df["LINKEDIN"].apply(lambda x: standardize_url(x))
df["FACEBOOK"] = df["FACEBOOK"].apply(lambda x: standardize_url(x))
df["DOMAIN"] = df["DOMAIN"].apply(lambda x: standardize_url(x))
save_df_to_csv(df, source=source)


source = "cb_org"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["city"] = df["ORGANIZATION_CITY"].apply(lambda x: standardize_city(x))
df["state"] = df["ORGANIZATION_STATE_CODE"].apply(lambda x: standardize_state(x, return_type="code"))
df["country"] = df["ORGANIZATION_COUNTRY_CODE"].apply(lambda x: standardize_country(x, return_type="code"))
df["TWITTER"] = df["TWITTER"].apply(lambda x: standardize_url(x))
df["LINKEDIN"] = df["LINKEDIN"].apply(lambda x: standardize_url(x))
df["DOMAIN"] = df["DOMAIN"].apply(lambda x: standardize_url(x))
save_df_to_csv(df, source=source)

source = "cb_org_institutions"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_parent"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_person"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["city"] = df["CITY"].apply(lambda x: standardize_city(x))
df["state"] = df["STATE_CODE"].apply(lambda x: standardize_state(x, return_type="code"))
df["country"] = df["COUNTRY_CODE"].apply(lambda x: standardize_country(x, return_type="code"))
df["TWITTER"] = df["TWITTER"].apply(lambda x: standardize_url(x))
df["FACEBOOK"] = df["FACEBOOK"].apply(lambda x: standardize_url(x))
df["LINKEDIN"] = df["LINKEDIN"].apply(lambda x: standardize_url(x))
save_df_to_csv(df, source=source)

source = "cb_person_degree"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "cb_person_to_org_current"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["MATCHED_TITLE"] = df["TITLE"].apply(lambda x: standardize_job_title(x))
save_df_to_csv(df, source=source)

source = "cb_person_to_org_former"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["MATCHED_TITLE"] = df["TITLE"].apply(lambda x: standardize_job_title(x))
save_df_to_csv(df, source=source)

source = "ss_org"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["city"] = df["ORGANIZATION_CITY"].apply(lambda x: standardize_city(x))
df["state"] = df["ORGANIZATION_STATE_CODE"].apply(lambda x: standardize_state(x, return_type="code"))
df["country"] = df["ORGANIZATION_COUNTRY_CODE"].apply(lambda x: standardize_country(x, return_type="code"))
df["TWITTER"] = df["TWITTER"].apply(lambda x: standardize_url(x))
df["LINKEDIN"] = df["LINKEDIN"].apply(lambda x: standardize_url(x))
df["DOMAIN"] = df["DOMAIN"].apply(lambda x: standardize_url(x))
df["FACEBOOK"] = df["FACEBOOK"].apply(lambda x: standardize_url(x))
save_df_to_csv(df, source=source)

source = "ss_parent"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
save_df_to_csv(df, source=source)

source = "ss_person"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["city"] = df["CITY"].apply(lambda x: standardize_city(x))
df["state"] = df["STATE_CODE"].apply(lambda x: standardize_state(x, return_type="code"))
df["country"] = df["COUNTRY_CODE"].apply(lambda x: standardize_country(x, return_type="code"))
df["TWITTER"] = df["TWITTER"].apply(lambda x: standardize_url(x))
df["FACEBOOK"] = df["FACEBOOK"].apply(lambda x: standardize_url(x))
df["LINKEDIN"] = df["LINKEDIN"].apply(lambda x: standardize_url(x))
df["WEBSITE"] = df["WEBSITE"].apply(lambda x: standardize_url(x))
save_df_to_csv(df, source=source)

source = "ss_person_to_org_current"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["MATCHED_TITLE"] = df["TITLE"].apply(lambda x: standardize_job_title(x))
save_df_to_csv(df, source=source)

source = "ss_person_to_org_former"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["MATCHED_TITLE"] = df["TITLE"].apply(lambda x: standardize_job_title(x))
save_df_to_csv(df, source=source)

source = "industry"
df = get_df_for_industry()
save_df_to_csv(df, source=source)

source = "ss_org_industry"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["INDUSTRY"] = df["INDUSTRY"].apply(lambda x: standardize_ss_industry(x))
df = df.explode("INDUSTRY")
df.drop_duplicates(inplace = True, ignore_index = True)
df = reduce_industry_df(df, "INDUSTRY")
save_df_to_csv(df, source=source)


source = "cb_org_industry"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
df["INDUSTRY"] = df["INDUSTRY"].apply(lambda x: x.split(","))
df["INDUSTRY"] = df["INDUSTRY"].apply(lambda x: standardize_cb_industry(x))
df = df.explode("INDUSTRY")
df.drop_duplicates(inplace = True, ignore_index = True)
df = reduce_industry_df(df, "INDUSTRY")
save_df_to_csv(df, source=source)
#%% md
## utils.py
#%%
from data_model.nodes import NODES
from data_model.relationships import RELATIONSHIPS
from utility.snowflake_master import snowflake_connector
from utility.neo4j_master import neo4j_connector
from utility.ut_env import configs
from utility.logger import logger
from geocode.geocode import Geocode
import pandas as pd

import re
import numpy as np
from fuzzy_match import process
from urllib.parse import urlparse

gc = Geocode()
gc.load()

DATA_TYPE_MAP = {
    "string": str,
    "integer": int,
    "float": float,
}

BATCH_SIZE = 10_000

INDUSTRIES = {'3D Printing', 'Accounting', 'Advertising', 'Advice', 'Aerospace', 'Agriculture', 'Analytics', 'Apps', 'Architecture', 'Art', 'Artificial Intelligence',
              'Asset Management', 'Association', 'Audio', 'Auto Insurance', 'Automotive', 'B2B', 'Banking', 'Beauty', 'Big Data', 'Biotechnology', 'Blockchain', 'Brand Marketing',
              'Broadcasting', 'Building Maintenance', 'Building Material', 'Business Development', 'Business Intelligence', 'CRM', 'Cannabis', 'Charity', 'Chemical', 'Child Care',
              'Civil Engineering', 'Cloud Computing', 'Cloud Data Services', 'Commercial', 'Commercial Insurance', 'Commercial Real Estate', 'Communities', 'Compliance', 'Computer',
              'Construction', 'Consulting', 'Consumer', 'Consumer Electronics', 'Consumer Goods', 'Content', 'Cosmetics', 'Creative Agency', 'Cryptocurrency', 'Customer Service',
              'Cyber Security', 'Database', 'Delivery', 'Dental', 'Digital Marketing', 'Digital Media', 'ECommerce', 'ELearning', 'Ecommerce', 'EdTech', 'Education',
              'Electrical Distribution', 'Electronics', 'Employment', 'Energy', 'Engineering', 'Enterprise Software', 'Environmental Consulting', 'Environmental Engineering',
              'Event Management', 'Events', 'Facilities Support Services', 'Facility Management', 'Farming', 'Fashion', 'FinTech', 'Finance', 'Financial Services', 'Fitness',
              'Food Processing', 'Food and Beverage', 'Freight Service', 'Furniture', 'Gaming', 'Government', 'Graphic Design', 'Hardware', 'Health Care', 'Health Diagnostics',
              'Health Insurance', 'Heath Care', 'Higher Education', 'Home Decor', 'Home Health Care', 'Home Improvement', 'Home Services', 'Hospital', 'Hospitality', 'Human Resources',
              'IT Infrastructure', 'IT Management', 'Industrial', 'Industrial Automation', 'Industrial Engineering', 'Industrial Manufacturing', 'Information Services',
              'Information Technology', 'Infrastructure', 'Insurance', 'Interior Design', 'Internet', 'Internet of Things', 'Law Enforcement', 'Leasing', 'Legal', 'Leisure', 'Lending',
              'Life Insurance', 'Life Science', 'Lifestyle', 'Lighting', 'Logistics', 'Machine Learning', 'Machinery Manufacturing', 'Management Consulting', 'Manufacturing', 'Market Research',
              'Marketing', 'Marketplace', 'Mechanical Engineering', 'Media and Entertainment', 'Medical', 'Medical Device', 'Military', 'Mining', 'Mobile', 'Mobile Apps', 'Music',
              'Network Security', 'News', 'Non Profit', 'Nursing and Residential Care', 'Oil and Gas', 'Online Portals', 'Outsourcing', 'Packaging Services', 'Payments', 'Personal Care',
              'Personal Health', 'Pharmaceutical', 'Photography', 'Plastics and Rubber Manufacturing', 'Printing', 'Product Design', 'Professional Services', 'Project Management',
              'Property Development', 'Property Management', 'Public Relations', 'Public Safety', 'Publishing', 'Real Estate', 'Real Estate Investment', 'Recreation', 'Recruiting', 'Recycling',
              'Rehabilitation', 'Renewable Energy', 'Rental', 'Rental Property', 'Research & Development', 'Residential', 'Restaurants', 'Retail', 'Retirement', 'Risk Management', 'Robotics',
              'SEO', 'SaaS', 'Sales', 'Security', 'Service Industry', 'Shipping', 'Shopping', 'Small and Medium Businesses', 'Social', 'Social Media', 'Social Media Marketing', 'Software',
              'Software Engineering', 'Solar', 'Sporting Goods', 'Sports', 'Staffing Agency', 'Supply Chain Management', 'Sustainability', 'Technical Support', 'Technology', 'Telecommunications',
              'Test and Measurement', 'Textiles', 'Therapeutics', 'Tourism', 'Training', 'Transportation', 'Travel', 'Venture Capital', 'Veterinary', 'Video', 'Video Games', 'Warehousing',
              'Waste Management', 'Water', 'Wealth Management', 'Web Apps', 'Web Design', 'Web Development', 'Web Hosting', 'Wellness', 'Wholesale', 'Wine And Spirits', 'Wireless', 'iOS'}

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


def run_cypher_query(cypher_query, return_type="ndarray"):
    """
    :param cypher_query: cypher query
    :param return_type: can be one of: ndarray, data_frame, subgraph
    :return: n-dim array object corresponding to the results of the input cypher query
    """
    if return_type == "ndarray":
        return neo4j_connector.run(cypher_query).to_ndarray()
    elif return_type == "data_frame":
        return neo4j_connector.run(cypher_query).to_data_frame()
    else:
        return neo4j_connector.run(cypher_query).to_subgraph()


def get_fields_for_source(source, nodes=NODES, relationships=RELATIONSHIPS):
    """
    :param source:
    :param nodes:
    :param relationships:
    :return: all the fields required from a given source
    """
    fields = set()
    for node in NODES:
        if node["source"] == source:
            for property in node["properties_list"]:
                fields.add(property["field"])

    for relation in RELATIONSHIPS:
        if relation["source"] == source:
            for property in relation["properties_list"]:
                fields.add(property["field"])
            fields.add(relation["start_node_key"][1]["field"])
            fields.add(relation["end_node_key"][1]["field"])

    return fields


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
    stand_url = str(urlparse(url).netloc or '') + str(urlparse(url).path or '')
    stand_url = stand_url.lstrip('www.')
    stand_url = stand_url.rstrip('/')
    return stand_url


def standardize_city(x):
    """
    :param x:
    :return: cleaned city name which doesn't vary across data source
    """
    if not isinstance(x, str):
        return None
    code = gc.decode('city ' + x)
    if not code:
        return None
    return code[0]['official_name']


def standardize_state(x, return_type="code"):
    """
    :param x:
    :param return_type: "code" or "name"
    :return:
    """
    if not isinstance(x, str):
        return None
    code = gc.decode('state ' + x)
    if not code:
        return None


def standardize_country(x, return_type="code"):
    """
    :param x:
    :param return_type: "code" or "name"
    :return:
    """
    if not isinstance(x, str):
        return None
    code = gc.decode('country ' + x)
    if not code:
        return None
    return code[0]['official_name']


def baseline_cleaning_helper(title):
    title = title.replace('-', "")
    title = re.sub(r'[^\s\w\d]', ",", title)
    title = re.sub(r'[0-9]', "", title)
    title = title.replace('SVP', "SENIOR VICE PRESIDENT")
    title = title.replace('FXD INC', "FIXED INCOME")
    title = title.replace('SR', "SENIOR")
    title = title.replace('VP', "VICE PRESIDENT")
    title = title.replace('CEO', ",CHIEF EXECUTIVE OFFICER,")
    title = title.replace('INVTS', "INVESTMENTS")
    title = title.replace('ADMIN ', "ADMINISTRATIVE")
    title = title.replace('OFICER', "OFFICER")
    title = title.replace('OPS', "OPERATIONS")
    title = title.replace('SENIOR ', 'SENIOR-')
    title = title.replace('MANAGING DIRECTOR', 'MANAGING-DIRECTOR')
    title = title.replace('VICE PRESIDENT', 'VICE-PRESIDENT')
    title = title.replace('ASSOCIATE DIRECTOR', 'ASSOCIATE-DIRECTOR')
    title = title.replace('OF ', "")
    title = title.replace('THE ', "")
    return title


def abbreviation_helper(title):
    abbrev_dict = {"CTO": "CHIEF TECHNOLOGY OFFICER",  "CRO": "CHIEF REVENUE OFFICER",
                   "CEO": "CHIEF EXECUTIVE OFFICER", "CFO": "CHIEF FINANCIAL OFFICER",
                   "COO": "CHIEF OPERATIONS OFFICER", "CMO": "CHIEF MARKETING OFFICER",
                   "CIO": "CHIEF INVESTMENT OFFICER", "CSO": "CHIEF STRATEGY OFFICER",
                   "CHRO": "CHIEF HUMAN RESOURCES OFFICER", "GM": "GENERAL MANAGER",
                   "CCO": "CHIEF COMMERICAL OFFICER", "CPO": "CHIEF PRODUCT OFFICER",
                   "MD": "MANAGING DIRECTOR", "COCEO": "COCHIEF EXECUTIVE OFFICER"}
    if title in abbrev_dict:
        return abbrev_dict[title]
    else:
        return title


def check_redundancies_helper(titles_list):
    no_redunancies = set()
    redundancy_map = {'CHAIR': 'CHAIRPERSON', 'CHAIRMAN': 'CHAIRPERSON', 'CHAIRMAN BOARD': 'CHAIRPERSON',
                      'CHAIRMAN BOARD DIRECTORS': 'CHAIRPERSON',
                      'BUSINESS DEVELOPMENT DIRECTOR': 'DIRECTOR BUSINESS DEVELOPMENT',
                      'CO CHIEF EXECUTIVE OFFICER': 'CHIEF EXECUTIVE OFFICER', 'CO FOUNDER': 'FOUNDER',
                      'CO OWNER': 'OWNER', 'CO PRESIDENT': 'PRESIDENT', 'COMMERCIAL DIRECTOR': 'COMMERCIAL',
                      'COMMERCIAL MANAGER': 'COMMERCIAL', 'COMPANY OWNER': 'OWNER',
                      'COOWNER': 'OWNER', 'EVICE PRESIDENT': 'EXECUTIVE VICE PRESIDENT',
                      'FINANCE DIRECTOR': 'DIRECTOR FINANCE', 'FINANCIAL DIRECTOR': 'DIRECTOR FINANCE',
                      'MANAGING-DIRECTOR': 'MANAGING DIRECTOR', 'MARKETING DIRECTOR': 'DIRECTOR MARKETING',
                      'MEMBER BOARD': 'BOARD MEMBER', 'MEMBER BOARD DIRECTORS': 'BOARD MEMBER',
                      'BOARD DIRECTORS': 'BOARD MEMBER', 'OPERATIONS DIRECTOR': 'DIRECTOR OPERATIONS',
                      'PRODUCT MANAGEMENT': 'PRODUCT MANAGER', 'SALES DIRECTOR': 'DIRECTOR SALES',
                      'DEVELOPER': 'SOFTWARE ENGINEER',
                      'SOFTWARE DEVELOPER': 'SOFTWARE ENGINEER', 'SENIOR-ADVISOR': 'SENIOR-ADVISOR',
                      'SENIOR-ASSOCIATE': 'SENIOR ASSOCIATE', 'SENIOR-CONSULTANT': 'SENIOR CONSULTANT',
                      'SENIOR-DIRECTOR': 'SENIOR DIRECTOR', 'SENIOR-MANAGER': 'SENIOR MANAGER',
                      'SENIOR-MANAGING-DIRECTOR': 'SENIOR MANAGING DIRECTOR',
                      'SENIOR-PARTNER': 'SENIOR PARTNER', 'SENIOR-VICE-PRESIDENT': 'SENIOR  VICE PRESIDENT',
                      'CHIEF OPERATING OFFICER' : 'CHIEF OPERATIONS OFFICER'},
    for title in titles_list:
        if title in redundancy_map:
            no_redunancies.add(redundancy_map[title])
        else:
            no_redunancies.add(title)
    return no_redunancies


def standardize_job_title(title):
    """
    :param title:
    :return: job title that maps to job node
    """
    simple_title_set = {'ADVISOR', 'ANALYST', 'ASSISTANT', 'ASSOCIATE', 'ASSOCIATE-DIRECTOR', 'DIRECTOR', 'MANAGER',
                        'PRESIDENT', 'OWNER', 'FOUNDER', 'CONSULTANT', 'ADVISOR', 'PARTNER', 'INVESTOR',
                        'SENIOR-ADVISOR', 'SENIOR-ASSOCIATE', 'SENIOR-CONSULTANT', 'SENIOR-DIRECTOR', 'SENIOR-MANAGER',
                        'SENIOR-MANAGING-DIRECTOR', 'SENIOR-PARTNER', 'SENIOR-VICE-PRESIDENT', 'INTERN',
                        'VICE-PRESIDENT', 'SENIOR-PRESIDENT'}
    choices = ['ACCOUNT DIRECTOR', 'ACCOUNT EXECUTIVE', 'ACCOUNT MANAGER', 'ADMINISTRATOR', 'ADVISOR',
               'ADVISORY BOARD MEMBER', 'ANALYST', 'ART DIRECTOR', 'ASSISTANT', 'ASSOCIATE', 'ASSOCIATE DIRECTOR',
               'BOARD DIRECTORS', 'BOARD MEMBER', 'BOARD OBSERVER', 'BRANCH MANAGER', 'BUSINESS ANALYST',
               'BUSINESS DEVELOPMENT', 'BUSINESS DEVELOPMENT DIRECTOR', 'BUSINESS DEVELOPMENT MANAGER',
               'BUSINESS MANAGER', 'BUSINESS OWNER', 'CHAIR', 'CHAIRMAN', 'CHAIRMAN BOARD',
               'CHAIRMAN BOARD DIRECTORS', 'CHAIRPERSON', 'CHIEF ADMINISTRATIVE OFFICER', 'CHIEF COMMERCIAL OFFICER',
               'CHIEF CREATIVE OFFICER', 'CHIEF EXECUTIVE OFFICER', 'CHIEF FINANCIAL OFFICER',
               'CHIEF INFORMATION OFFICER', 'CHIEF INVESTMENT OFFICER', 'CHIEF MARKETING OFFICER',
               'CHIEF MEDICAL OFFICER', 'CHIEF OPERATING OFFICER', 'CHIEF OPERATIONS OFFICER', 'CHIEF PRODUCT OFFICER',
               'CHIEF REVENUE OFFICER', 'CHIEF SCIENTIFIC OFFICER', 'CHIEF STRATEGY OFFICER', 'CHIEF TECH/SCI/R&D OFFICER',
               'CHIEF TECHNOLOGY OFFICER', 'CLINICAL DIRECTOR', 'CO FOUNDER', 'CO OWNER', 'CO PRESIDENT',
               'COMMERCIAL DIRECTOR', 'COMMERCIAL MANAGER', 'COMMUNICATIONS', 'COMPANY OWNER', 'COMPLIANCE OFFICER',
               'CONSULTANT', 'CONTROLLER', 'COOWNER', 'CORPORATE DEVELOPMENT', 'CORPORATE OFFICER',
               'CORPORATE SECRETARY', 'CREATIVE DIRECTOR', 'DEPUTY DIRECTOR', 'DEVELOPER', 'DIRECTOR',
               'DIRECTOR BACK OFFICE OPERATION', 'DIRECTOR BUSINESS DEVELOPMENT', 'DIRECTOR ENGINEERING',
               'DIRECTOR FINANCE', 'DIRECTOR GENERAL', 'DIRECTOR MARKETING', 'DIRECTOR INVESTMENTS',
               'DIRECTOR RESEARCH EQUITY', 'DIRECTOR RESEARCH FIXED INCOME', 'DIRECTOR OPERATIONS', 'DIRECTOR SALES',
               'DOCTORATE DEGREE', 'ECONOMIST', 'ENGINEERING', 'EVICE PRESIDENT', 'EXECUTIVE CHAIRMAN',
               'EXECUTIVE DIRECTOR', 'EXECUTIVE PARTNER', 'EXECUTIVE VICE PRESIDENT', 'EXPORT MANAGER',
               'FINANCE', 'FINANCE DIRECTOR', 'FINANCE MANAGER', 'FINANCIAL DIRECTOR', 'FOUNDER',
               'FOUNDING DIRECTOR', 'FOUNDING MEMBER', 'FOUNDING PARTNER', 'GENERAL COUNSEL', 'GENERAL DIRECTOR',
               'GENERAL MANAGER', 'GENERAL PARTNER', 'GRADUATE DEGREE', 'HEAD EQUITY INVESTMENTS', 'HEAD FIXED INCOME INVESTMENTS',
               'HEAD MARKETING','HEAD GOVERNMENT', 'HEAD PRIVATE BANKING',
               'HEAD STATE', 'HEAD PRODUCT', 'HEAD SALES', 'HUMAN RESOURCES OFFICER', 'INDEPENDENT DIRECTOR',
               'INSTITUTIONAL SALES', 'INTERN', 'INVESTMENT COMMITTEE MEMBER', 'INVESTOR', 'INVESTOR RELATIONS CONTACT',
               'MANAGER', 'MANAGING DIRECTOR', 'MANAGING MEMBER',
               'MANAGING PARTNER', 'MANAGING PRINCIPAL', 'MARKET STRATEGIST', 'MARKETING', 'MARKETING DIRECTOR',
               'MARKETING MANAGER', 'MASTERS BUSINESS ADMIN', 'MEDIA', 'MEDICAL DIRECTOR', 'MEMBER BOARD',
               'MEMBER BOARD DIRECTORS', 'MENTOR', 'MINISTER OF GOVERNMENT',
               'NATIONAL SALES MANAGER', 'NON EXECUTIVE DIRECTOR', 'OFFICE MANAGER', 'OPERATIONS',
               'OPERATIONS DIRECTOR', 'OPERATIONS MANAGER', 'OWNER', 'PARTNER', 'PARTNERSHIPS',
               'PORTFOLIO MANAGER EQUITIES', 'PORTFOLIO MANAGER FIXED INCOME', 'PRESIDENT',
               'PRINCIPAL', 'PRINCIPAL CONSULTANT', 'PRINCIPAL OWNER', 'PRIVATE EQUITY ANALYST',
               'PRIVATE EQUITY INVESTOR', 'PRODUCT', 'PRODUCT DEVELOPMENT', 'PRODUCT MANAGEMENT', 'PRODUCT MANAGER',
               'PRODUCT OWNER', 'PRODUCTION MANAGER', 'PROFESSOR', 'PROGRAM MANAGER',
               'PROJECT DIRECTOR', 'PROJECT MANAGER', 'PUBLIC COMMUNICATIONS CONTACT', 'REGIONAL DIRECTOR',
               'REGIONAL MANAGER', 'REGIONAL SALES MANAGER', 'REPRESENTATIVE DIRECTOR', 'RESEARCH',
               'RESEARCH ASSISTANT', 'SALES', 'SALES DIRECTOR', 'SALES EXECUTIVE',
               'SALES MANAGER', 'SALES REPRESENTATIVE', 'SECRETARY', 'SENIOR ADVISOR', 'SENIOR ASSOCIATE',
               'SENIOR CONSULTANT', 'SENIOR DIRECTOR', 'SENIOR MANAGER', 'SENIOR MANAGING DIRECTOR', 'SENIOR PARTNER',
               'SENIOR PROJECT MANAGER', 'SENIOR SOFTWARE ENGINEER', 'SENIOR VICE PRESIDENT',
               'SHAREHOLDER', 'SHARIAH BOARD MEMBER', 'SOFTWARE DEVELOPER', 'SOFTWARE ENGINEER', 'STRATEGY',
               'TECHNICAL DIRECTOR', 'TRADING EQUITY', 'TRADING FIXED INCOME', 'TREASURER', 'UNDERGRADUATE DEGREE',
               'VICE CHAIRMAN', 'VICE PRESIDENT', 'VICE PRESIDENT BUSINESS DEVELOPMENT',
               'VICE PRESIDENT ENGINEERING', 'VICE PRESIDENT FINANCE', 'VICE PRESIDENT MARKETING',
               'VICE PRESIDENT OPERATIONS', 'VICE PRESIDENT SALES']
    title = baseline_cleaning_helper(title)
    title_alt = title.replace(' AND ', ",")
    title_alt = title_alt.replace(' ,', ",")
    title_alt = title_alt.replace(', ', ",")
    title_alt = title_alt.replace(' , ', ",")
    title_list = title_alt.split(',')
    df = pd.DataFrame(title_list, columns=["titles_split"])
    df["cleaned"] = df["titles_split"].apply(lambda x: abbreviation_helper(x)).str.upper()
    df["match"] = df["cleaned"].apply(lambda x: process.extract(x, choices, limit=1, scorer='ratio'))
    df["match_clean"] = df["match"].apply(lambda x: x[0][0] if x[0][1] > 85 else np.nan)
    df.dropna(inplace=True, how="any")
    to_ret = set(df["match_clean"].to_list())
    token_list = title.split(" ")
    for token in token_list:
        if token in simple_title_set:
            to_ret.add(token)
    to_ret = check_redundancies_helper(to_ret)
    to_ret = list(to_ret)
    if len(to_ret) == 0:
        to_ret = ["UNCATEGORIZED"]
    return to_ret


def standardize_ss_industry(ind: str):
    to_ret = set()
    ss_to_cb_map = {'3D Printing': ['3D Printing'], 'Aerospace & Defense': ['Aerospace', 'Military'], 'Agriculture': ['Agriculture'], 'Architecture': ['Architecture'],
                    'Asset Management': ['Asset Management'], 'Audio/Visual': ['Audio', 'Video'], 'Automotive': ['Automotive'], 'Automotive Aftermarket': ['Automotive'],
                    'Banking': ['Banking'], 'Behavioral Health': ['Heath Care', 'Personal Health'], 'Big Data': ['Big Data'], 'Biotechnology': ['Biotechnology'],
                    'Business Services': ['Business Development'], 'Cannabis': ['Cannabis'], 'Chemical': ['Chemical'], 'Compliance': ['Compliance'], 'Construction': ['Construction'],
                    'Consumer': ['Consumer'], 'Content Management': ['Content'], 'Customer Service': ['Customer Service'], 'Cyber Security': ['Cyber Security'], 'Dental': ['Dental'],
                    'Design & Automation': ['Industrial Automation'], 'Digital Media': ['Digital Media'], 'Early Childhood': ['Child Care'], 'Ecommerce': ['Ecommerce'],
                    'Education': ['Education'], 'Energy': ['Energy'], 'Engineering': ['Engineering'], 'Environmental Services': ['Environmental Consulting'],
                    'Facilities Management': ['Facility Management'], 'Finance & Accounting': ['Accounting', 'Finance'], 'Financial Services': ['Financial Services'],
                    'Financial Technology': ['FinTech'], 'Food & Beverage': ['Food and Beverage'], 'Franchise & Restaurants': ['Restaurants'], 'Gaming': ['Gaming'],
                    'Government Services': ['Government'], 'Graphic Design': ['Graphic Design'], 'Health & Wellness': ['Wellness', 'Personal Health'], 'Healthcare': ['Health Care'],
                    'Healthcare Services': ['Health Care'], 'Healthcare Technology': ['Health Care'], 'Higher Education': ['Higher Education'], 'Hospitality': ['Hospitality'],
                    'Human Resources': ['Human Resources'], 'Industrial': ['Industrial'], 'Industrial Automation': ['Industrial Automation'], 'Information Services': ['Information Services'],
                    'Infrastructure Services': ['Infrastructure'], 'Insurance': ['Insurance'], 'Internet': ['Internet'], 'Internet of Things': ['Internet of Things'], 'Legal': ['Legal'],
                    'Lending': ['Lending'], 'Life Sciences': ['Life Science'], 'Manufacturing': ['Manufacturing'], 'Media': ['Media and Entertainment'], 'Medical Devices': ['Medical Device'],
                    'Metals & Mining': ['Mining'], 'Mobile': ['Mobile'], 'Mortgage Banking': ['Banking'], 'Non-profit': ['Non Profit'], 'Oil & Gas': ['Oil and Gas'],
                    'Ophthalmology': ['Health Care'], 'Optometry': ['Health Care'], 'Packaging': ['Packaging Services'], 'Payments': ['Payments'], 'Personal Care': ['Personal Health'],
                    'Pet Products': ['Consumer Goods'], 'Pharmaceutical': ['Pharmaceutical'], 'Physical Therapy': ['Health Care', 'Personal Care'], 'Post-acute Care': ['Health Care'],
                    'Public Safety': ['Public Safety'], 'Radiology': ['Health Care'], 'Real Estate Services': ['Real Estate'], 'Remote Monitoring': ['Information Technology'],
                    'Research & Development': ['Research & Development'], 'Retail': ['Retail'], 'Revenue Cycle Management': ['Finance'], 'Sales & Marketing': ['Sales', 'Marketing'],
                    'Security': ['Security'], 'Specialty Pharmacy': ['Pharmaceutical'], 'Supply Chain & Logistics': ['Supply Chain Management', 'Logistics'],
                    'Tech-enabled Services': ['Technology'], 'Technology': ['Technology'], 'Telecom': ['Telecommunications'], 'Testing & Measurement': ['Test and Measurement'],
                    'Training': ['Training'], 'Transportation & Warehousing': ['Transportation', 'Warehousing'], 'Veterinary': ['Veterinary'], 'Waste Management': ['Waste Management'],
                    'Water': ['Water']}
    if ind in ss_to_cb_map:
        to_ret.update(ss_to_cb_map(ind))
    return to_ret

def standardize_cb_industry(ind_list: list):
    to_ret = set(ind_list)
    cb_technology = {"FinTech", "EdTech", "Information Technology", "Biotechnology"}
    cb_engineering = {"Industrial Engineering", "Mechanical Engineering", "Civil Engineering", "Environmental Engineering", "Software Engineering"}
    for industry in ind_list:
        if industry in cb_technology:
            to_ret.add("Technology")
        if industry in cb_engineering:
            to_ret.add("Engineering")
    return list(to_ret)

def get_df_for_industry():
    industries = list(INDUSTRIES)
    df = pd.DataFrame(industries, columns= ["INDUSTRY"])
    return df

def reduce_industry_df(df, col):
    df[col] = df[col].apply(lambda x: x if x in INDUSTRIES else np.nan)
    df.dropna(subset = [col], inplace = True)
    df.reset_index(inplace = True)
    return df