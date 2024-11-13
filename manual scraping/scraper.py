import requests
import json
import os
import time
import random

# Base URL for Instagram's GraphQL and search endpoints
base_url = "https://www.instagram.com"

# Define the path to the cookies file and usernames file
cookies_file = "cookies.json"
usernames_file = "usernames.txt"

# Load cookies from file if available, otherwise prompt for manual entry
def load_cookies():
    if os.path.exists(cookies_file):
        with open(cookies_file, "r") as file:
            return json.load(file)
    else:
        # Manually enter cookies only the first time
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

# Function to get user profile data by user ID
def get_profile_data(user_id, username, headers):
    # Directory to save JSON response
    output_dir = f"scraped/{username}"
    os.makedirs(output_dir, exist_ok=True)

    # URL for GraphQL endpoint
    url = f"{base_url}/graphql/query"

    # Data payload for the GraphQL query, with the user ID in `variables`
    data = {
        "variables": json.dumps({"id": user_id, "render_surface": "PROFILE"}),
        "doc_id": "8508998995859778"
    }

    # Send the POST request
    response = requests.post(url, headers=headers, data=data)

    # Save response to a JSON file if successful
    if response.status_code == 200:
        profile_data = response.json()
        json_path = os.path.join(output_dir, "profile.json")
        with open(json_path, "w") as json_file:
            json.dump(profile_data, json_file, indent=4)
        print(f"Full JSON data for {username} saved to {json_path}")
    else:
        print(f"Failed to retrieve profile data for {username}. Status code:", response.status_code)
        print("Response:", response.text)

# Main function to get profile data from a list of usernames
def main():
    # Load usernames from file
    if not os.path.exists(usernames_file):
        print(f"Usernames file '{usernames_file}' not found.")
        return

    with open(usernames_file, "r") as file:
        usernames = [line.strip() for line in file if line.strip()]

    if not usernames:
        print("No usernames found in the file.")
        return

    # Load the cookies from file (or prompt for them if the file doesn't exist)
    cookies = load_cookies()

    # Create headers and add the loaded cookies and csrf token
    headers = {
        "cookie": cookies,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-csrftoken": cookies.split('csrftoken=')[1].split(';')[0],  # Extract the CSRF token from cookies
        "x-ig-app-id": "936619743392459"
    }

    # Loop through each username, get user ID, and fetch profile data
    for username in usernames:
        print(f"Processing username: {username}")
        user_id = get_user_id(username, headers)
        if user_id:
            get_profile_data(user_id, username, headers)
            # Add a random delay between 5 and 10 seconds
            wait_time = random.randint(10, 15)
            print(f"Waiting for {wait_time} seconds to avoid rate limiting...")
            time.sleep(wait_time)
        else:
            print(f"Skipping {username} due to missing user ID.")

# Run the main function
if __name__ == "__main__":
    main()
