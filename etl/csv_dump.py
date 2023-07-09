# set the path from repo root to src
# import sys
# sys.path.append('src')
# set the repo root as the working directory
import os
os.chdir('/Users/victoriashi/GitHub/graph_ELT')

from etl.data_model.nodes import NODES
from data_model.relationships import RELATIONSHIPS
from data_model.constraints import CONSTRAINTS
from etl.utils import ingest_nodes, ingest_relationships, run_cypher_query


for constraint in CONSTRAINTS:
    run_cypher_query(constraint)

for node in NODES:
    ingest_nodes(node)

for relationship in RELATIONSHIPS:
    ingest_relationships(relationship)


source = "ss_org"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
# do transformations, if any
# standardize urls
df[""] = df[""].apply(lambda x: standardize_url(x, kind='linkedin'))
# standardize city name, state code, state name, country code, country name
df[""] = df[""].apply(lambda x: standardize_state(x, return_type="code"))
save_df_to_csv(df, source=source)


source = "cb_org"
df = get_df_from_snowflake(f"SELECT {', '.join(get_fields_for_source(source))} FROM l2_new.graph_{source}")
# do transformations, if any
# standardize urls
# standardize city name, state code, state name, country code, country name
save_df_to_csv(df, source=source)