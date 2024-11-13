import json
import pandas as pd

with open('./out/people.json', 'r') as f:
    data = json.loads(f.read())

    nodes = []
    edges = []

    for person_id, person_data in data.items():
        # add current person as node

        general = person_data['general']
        nodes.append({
            'id:': general['id'],
            'label': general['username'],
            'full_name': general['full_name'],
            'is_private': general['is_private'],

        })

        followings = person_data['followings']

        for follow in followings:
            nodes.append({
            'id:': follow['pk'],
            'label': follow['username'],
            'full_name': follow['full_name'],
            'is_private': follow['is_private']
            })

        for follow in followings:
            edges.append({
                'source': person_id,
                'target': follow['pk']
            })

nodes_df = pd.DataFrame.from_dict(nodes)
edges_df = pd.DataFrame.from_dict(edges)


nodes_df.to_csv('./out/graph/nodes.csv', index=False, header=True)
edges_df.to_csv('./out/graph/edges.csv', index=False, header=True)