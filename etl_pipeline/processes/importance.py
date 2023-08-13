from etl.utils import run_cypher_query
"""
Functions that can be used:
    - gds.pageRank 
    - gds.betweenness 
"""



# def get_top_n(res, lim: int):
#     run_cypher_query(f"""MATCH (n {res}) RETURN n LIMIT {lim}""")


execution_mode = "stream"
result = None

for centrality_measure in ["pagerank", "betweenness"]:
    for sector in ["non_profit", "for_profit"]:
        for unit in ["org", "person"]:
            # create a new projection
            projection_name = f"{sector}_{unit}_{centrality_measure}"
            # print(projection_name)
            projection_query = f"""
                CALL gds.graph.project(
                {projection_name}, 
            )
            """
            result = run_cypher_query(projection_query)

            # run the pagerank algorithm in stream mode
            query = f"""
                CALL gds.pageRank.{execution_mode}(
                    {projection_name}, 
            )
            """
            result = run_cypher_query(projection_query)

            # drop query to free up memory
            drop_query = f"""
                CALL gds.graph.drop(
                    {projection_name}
                )
            """
            result = run_cypher_query(drop_query)



"""
Projection 1: 10 most important in for-profit organizations (pagerank)

Projection 2: 10 most important in non-profit organizations (pagerank)

Projection 3: 30 most important people in for-profit organizations (pagerank)

Projection 4: 30 most important people in non-profit organizations (pagerank)
"""


#  shared attributes:
unit = "org"
centrality_measure = "pagerank"
execution_mode = "stream"

# individual attributes
sector = "for_profit"
projection_name = f"{sector}_{unit}_{centrality_measure}_importance"

projection_query = f"""
    CALL gds.graph.project(
    {projection_name}, 
)
"""
result = run_cypher_query(projection_query)

query = f"""
    CALL gds.pageRank.{execution_mode}(
        {projection_name}, 
)
"""
result = run_cypher_query(query)

# free up memory
drop_query = f"""
    CALL gds.graph.drop(
        {projection_name}
    )
"""
result = run_cypher_query(drop_query)
get_top_n(result, 10)

# free up memory
drop_query = f"""
    CALL gds.graph.drop(
        {projection_name}
    )
"""
result = run_cypher_query(drop_query)
"""
Projection 2: 10 most important non-profit organizations by pagerank importance
"""

sector = "non_profit"
projection_name = f"{sector}_{unit}_{centrality_measure}_importance"

projection_query = f"""
    CALL gds.graph.project(
    {projection_name}, 
)
"""
result = run_cypher_query(projection_query)

query = f"""
    CALL gds.pageRank.{execution_mode}(
        {projection_name}, 
    )
"""
result = run_cypher_query(query)

drop_query = f"""
    CALL gds.graph.drop(
        {projection_name}
    )
"""
result = run_cypher_query(drop_query)

"""
Projection 3: 10 most important people in for-profit organizations by pagerank importance
"""
#  shared attributes:
unit = "person"
centrality_measure = "pagerank"

#  individual attributes:
sector = "for_profit"
projection_name = f"{sector}_{unit}_{centrality_measure}_importance"

projection_query = f"""
    CALL gds.graph.project(
    {projection_name}, 
)
"""
result = run_cypher_query(projection_query)

# run the pagerank algorithm
query = f"""
    CALL gds.pageRank.{execution_mode}(
        {projection_name}, 
)
"""
result = run_cypher_query(query)
get_top_n(result, 10)

drop_query = f"""
    CALL gds.graph.drop(
        {projection_name}
    )
"""
result = run_cypher_query(drop_query)

"""
Projection 4: 10 most organizations people in non-profit organizations by pagerank importance
"""
#  shared attributes:
sector = "non_profit"
centrality_measure = "pagerank"

projection_name = f"{sector}_{unit}_{centrality_measure}_importance"

projection_query = f"""
    CALL gds.graph.project(
    {projection_name}, 
)
"""
result = run_cypher_query(projection_query)

query = f"""
    CALL gds.pageRank.{execution_mode}(
        {projection_name}, 
)
"""
result = run_cypher_query(query)

drop_query = f"""
    CALL gds.graph.drop(
        {projection_name}
    )
"""
result = run_cypher_query(drop_query)

