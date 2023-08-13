import json
import pandas as pd
from igraph import Graph as ig


def parse_json(file):
    """
    deal with the input in json format
    :rtype: dict
    :param file:  file name
    :return: list of dicts
    """
    with open(file, 'r', encoding='utf_8_sig') as f:
        content = f.read()
        # print(content)
        # necessarily, the beginning of file is an illegal character for utf-8
        if content.startswith(u'\ufeff'):
            content = content.encode('utf8')[3:].decode('utf8')
        # other processing
        content = content.replace('\\', '\\\\')
        # print(content)
        load_dict = json.loads(content, strict=False)
    return load_dict


json_records = parse_json('records.json')

# extract the information of nodes and edges
matched_rels = []
# records that do not have matched fields
unmatched_rels = []

for r in json_records:
    try:
        if 'name' in r['source']['properties'] and 'name' in r['target']['properties']:
            matched_rels.append((r['source']['labels'][0] + ': ' + r['source']['properties']['name'],
                                 r['target']['labels'][0] + ': ' + r['target']['properties']['name']))
        elif 'name' in r['source']['properties'] and 'industry' in r['target']['properties']:
            matched_rels.append((r['source']['labels'][0] + ': ' + r['source']['properties']['name'],
                                 r['target']['labels'][0] + ': ' + r['target']['properties']['industry']))
        elif 'industry' in r['source']['properties'] and 'name' in r['target']['properties']:
            matched_rels.append((r['source']['labels'][0] + ': ' + r['source']['properties']['industry'],
                                 r['target']['labels'][0] + ': ' + r['target']['properties']['name']))
    except KeyError:
        unmatched_rels.append(r)

myGraph = ig(directed=True)
myGraph = myGraph.TupleList(matched_rels, weights=False, directed=True)
myGraph.get_edge_dataframe()
print(myGraph.vcount())

# node and nodeId
df_vertex = myGraph.get_vertex_dataframe()
# degree centrality
degree = myGraph.degree()
# closeness centrality
closeness = myGraph.closeness(normalized=True)
# betweenness centrality
betweenness = myGraph.betweenness()
# eigenvector centrality
eigenvector = myGraph.eigenvector_centrality()
# pagerank
personalized_pagerank = ig.personalized_pagerank(myGraph, damping=0.85, reset_vertices=None, weights=None)


df_vertex['degree'] = degree
df_vertex['closeness'] = closeness  # between 0 and 1
df_vertex['betweenness'] = betweenness
df_vertex['eigenvector'] = eigenvector
df_vertex['pagerank'] = personalized_pagerank
display(df_vertex.head())
df_vertex.to_excel('centrality_all.xlsx', index=None)

# # standardize centrality measures using min max normalization using pandas apply
# df_vertex = df_vertex.apply(lambda x: (x - df_vertex.min()) /
#                                                     (df_vertex.max() - df_vertex.min()), axis=0)
# print(df_vertex.head())
# df_vertex.to_excel('centrality_all_normalized.xlsx', index=False)
#

# %%
degree_dict = dict()
closeness_dict = dict()
betweenness_dict = dict()
eigenvector_dict = dict()
pagerank_dict = dict()

for r in range(len(df_vertex)):
    degree_dict[df_vertex['name'][r]] = df_vertex['degree'][r]
    closeness_dict[df_vertex['name'][r]] = df_vertex['closeness'][r]
    betweenness_dict[df_vertex['name'][r]] = df_vertex['betweenness'][r]
    eigenvector_dict[df_vertex['name'][r]] = df_vertex['eigenvector'][r]
    pagerank_dict[df_vertex['name'][r]] = df_vertex['pagerank'][r]

# coefficients of different centrality
a1 = 0.2  # coefficient of degree centrality divided by the sum
a2 = 0.2
a3 = 0.2
a4 = 0.2
a5 = 0.2

result = []
for r in matched_rels:
    weight = (a1 * (degree_dict[r[0]] + degree_dict[r[1]]) +
              a2 * (closeness_dict[r[0]] + closeness_dict[r[1]]) +
              a3 * (betweenness_dict[r[0]] + betweenness_dict[r[1]]) +
              a4 * (eigenvector_dict[r[0]] + eigenvector_dict[r[1]]) +
              a5 * (pagerank_dict[r[0]] + pagerank_dict[r[1]]))
    result.append([r[0], r[1], weight])

# dataframe with edge information: source, target, weight
df_edge = pd.DataFrame(result, columns=['source', 'target', 'weight'])
display(df_edge.head())
# %%

# write the centrality measures to excel
df_edge.to_excel('edge_all.xlsx', index=None)

