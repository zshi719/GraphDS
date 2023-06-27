
from data_model.nodes import NODES
from data_model.relationships import RELATIONSHIPS
from data_model.constraints import CONSTRAINTS
from etl.utils import ingest_nodes, ingest_relationships, execute_cypher_query


for constraint in CONSTRAINTS:
    execute_cypher_query(constraint)

for node in NODES:
    ingest_nodes(node)

for relationship in RELATIONSHIPS:
    ingest_relationships(relationship)
