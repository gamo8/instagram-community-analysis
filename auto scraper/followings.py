import requests
import json
import os
import csv
import time
import random

# Base URL for Instagram's GraphQL and API endpoints
base_url = "https://www.instagram.com"

# Define the path to the cookies file
cookies_file = "cookies.json"

# Load cookies from file if available, otherwise prompt for manual entry
def load_cookies():
    if os.path.exists(cookies_file):
        with open(cookies_file, "r") as file:
            return json.load(file)
    else:
        cookies = input("Enter your full cookie string: ")
        with open(cookies_file, "w") as file:
            json.dump(cookies, file)
        return cookies

# Function to get user ID from Instagram username
def get_user_id(username, headers):
    search_url = f"{base_url}/web/search/topsearch/"
    params = {"context": "blended", "query": username}
    response = requests.get(search_url, headers=headers, params=params)
    
    if response.status_code == 200:
        results = response.json().get("users", [])
        for user in results:
            if user["user"]["username"].lower() == username.lower():
                return user["user"]["pk"]
    print(f"User ID for {username} not found.")
    return None

# Function to save main account details in `account_info.csv`
def save_main_account_info(user_id, username, headers):
    output_file = "scraped/account_info.csv"
    url = f"{base_url}/api/v1/users/{user_id}/info/"

    # Make request to fetch main account's details
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json().get("user", {})
        if user_data:
            # Check if file exists, if not write the header
            file_exists = os.path.isfile(output_file)
            with open(output_file, mode="a", newline="", encoding="utf-8") as file:
                csv_writer = csv.writer(file)
                if not file_exists:
                    csv_writer.writerow(["id", "label", "full_name", "is_private", "profile_url"])
                
                csv_writer.writerow([
                    user_data.get("pk", ""),
                    user_data.get("username", ""),
                    user_data.get("full_name", ""),
                    user_data.get("is_private", False),
                    user_data.get("profile_pic_url", "")
                ])
        print(f"Main account info for {username} saved to {output_file}")
    else:
        print(f"Failed to fetch main account info for {username}. Status code: {response.status_code}")

# Function to fetch following details in batches
def fetch_following_details(user_ids, headers):
    url = f"{base_url}/api/v1/friendships/show_many/"
    user_ids_str = ",".join(user_ids)
    data = {"user_ids": user_ids_str}

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("friendship_statuses", {})
    else:
        print("Failed to fetch following details. Status code:", response.status_code)
        print("Response:", response.text)
        return {}

# Function to get following list with additional information and save to CSV
def get_following(user_id, username, headers):
    output_dir = "scraped"
    os.makedirs(output_dir, exist_ok=True)

    # CSV filename now includes `username` and `user_id`
    csv_path = os.path.join(output_dir, f"{username}_{user_id}_following_info.csv")
    with open(csv_path, mode="w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["id", "label", "full_name", "is_private", "profile_url"])

        has_next_page = True
        end_cursor = None

        while has_next_page:
            url = f"{base_url}/graphql/query"
            variables = {
                "id": user_id,
                "include_reel": False,
                "fetch_mutual": False,
                "first": 50
            }
            if end_cursor:
                variables["after"] = end_cursor

            data = {
                "variables": json.dumps(variables),
                "doc_id": "17874545323001329"  # doc_id for following
            }

            response = requests.get(url, headers=headers, params=data)

            if response.status_code == 200:
                json_response = response.json()
                page_info = json_response["data"]["user"]["edge_follow"]["page_info"]
                edges = json_response["data"]["user"]["edge_follow"]["edges"]

                user_ids = [edge["node"]["id"] for edge in edges]
                following_details = fetch_following_details(user_ids, headers)

                for edge in edges:
                    node = edge["node"]
                    target_id = node["id"]
                    label = node.get("username", "")
                    full_name = node.get("full_name", "")
                    is_private = following_details.get(target_id, {}).get("is_private", False)
                    profile_url = node.get("profile_pic_url", "")

                    # Write to CSV
                    csv_writer.writerow([target_id, label, full_name, is_private, profile_url])

                has_next_page = page_info["has_next_page"]
                end_cursor = page_info["end_cursor"]

                print(f"Fetched {len(edges)} followings so far for {username}...")

                time.sleep(random.randint(5, 10))  # Random delay
            else:
                print(f"Failed to retrieve following data for {username}. Status code:", response.status_code)
                print("Response:", response.text)
                break

    print(f"Following information saved to {csv_path}")

# Main function to process each username in `usernames.txt`
def main():
    cookies = load_cookies()

    headers = {
        "cookie": cookies,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-csrftoken": cookies.split('csrftoken=')[1].split(';')[0],
        "x-ig-app-id": "936619743392459"
    }

    # Load usernames from `usernames.txt`
    with open("usernames.txt", "r") as file:
        usernames = [line.strip() for line in file if line.strip()]

    # Ensure `account_info.csv` is saved in `scraped` directory
    os.makedirs("scraped", exist_ok=True)

    # Iterate over each username in the list
    for username in usernames:
        user_id = get_user_id(username, headers)
        if user_id:
            print(f"Fetching followings for {username} (ID: {user_id})...")
            save_main_account_info(user_id, username, headers)
            get_following(user_id, username, headers)
            # Adding a delay between requests to different accounts
            time.sleep(random.randint(10, 15))
        else:
            print(f"User ID for {username} not found. Skipping.")

# Run the main function
if __name__ == "__main__":
    main()
