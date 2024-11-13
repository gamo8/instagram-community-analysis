import os
import pandas as pd

# Directory paths
scraped_dir = "./scraped"
gephi_dir = "./gephi_input"

# Ensure gephi_input directory exists
os.makedirs(gephi_dir, exist_ok=True)

# Step 1: Collect edges from followings files
edges = []
followings_accounts = []

for filename in os.listdir(scraped_dir):
    if filename.endswith("_following_info.csv"):
        filepath = os.path.join(scraped_dir, filename)
        # Extract account ID from filename
        account_id = filename.split("_following_info")[0].split("_")[-1]


        followings_df = pd.read_csv(filepath)
        # Create edges with the main account as the source
        followings_df["source"] = account_id
        followings_df.rename(columns={"id": "target"}, inplace=True)
        edges.append(followings_df[["source", "target"]])

        # Add followings to the list for nodes collection
        followings_accounts.append(followings_df[["target", "label", "full_name", "is_private", "profile_url"]].rename(columns={"target": "id"}))

# Step 2: Concatenate all edges and remove exact duplicates
edges_df = pd.concat(edges, ignore_index=True).drop_duplicates()
edges_output_path = os.path.join(gephi_dir, "edges.csv")
edges_df.to_csv(edges_output_path, index=False)

# Step 3: Prepare nodes list by combining account_info.csv with followings data
account_info_path = os.path.join(scraped_dir, "account_info.csv")
main_accounts_df = pd.read_csv(account_info_path)

# Concatenate main accounts and following accounts
followings_df = pd.concat(followings_accounts, ignore_index=True)
nodes_df = pd.concat([main_accounts_df, followings_df], ignore_index=True)

# Step 4: Remove duplicate nodes based on 'id' to ensure uniqueness
nodes_df = nodes_df.drop_duplicates(subset=["id"])
nodes_output_path = os.path.join(gephi_dir, "nodes.csv")
nodes_df.to_csv(nodes_output_path, index=False)
