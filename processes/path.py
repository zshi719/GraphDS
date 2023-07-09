from etl.utils import run_cypher_query

"""
Functions that can be used:
    - gds.shortestPath.dijkstra 
"""


"""
Shortest paths 2 given persons in a relevant subgraph.
"""
source_person_id = ""
target_person_id = ""


"""
Shortest paths between a given person and the C-level (that is, CEO, CFO, etc) employees of a given company. 
"""
source_person_id = ""
target_company_id = ""


"""
Shortest paths between a given team/group of people and another given team/group of people. 
The teams could be specified explicitly or implicitly (like employees of a given company). 
"""
source_person_ids = []
