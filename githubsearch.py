#! /usr/bin/env python3

import requests
import os
import json
import getpass

# GitHub API endpoint
API_URL = "https://api.github.com"

# You should set this as an environment variable for security
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

def get_github_token():
    """Get the GitHub token from environment variable or user input."""
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GitHub token not found in environment variables.")
        token = getpass.getpass("Enter your GitHub Personal Access Token: ")
    return token

def print_curl_command(method, url, headers, data=None):
    """Print the equivalent curl command for a given request."""
    header_args = ' '.join([f"-H '{k}: {v}'" for k, v in headers.items()])
    data_arg = f"-d '{json.dumps(data)}'" if data else ""
    print(f"curl -X {method} {header_args} {data_arg} '{url}'")

def search_developer(username):
    """Search for a developer on GitHub and return their information."""
    url = f"{API_URL}/users/{username}"
    
    GITHUB_TOKEN = get_github_token()
    
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    print("\nEquivalent curl command for searching developer:")
    print_curl_command("GET", url, headers)
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    
    
    username = input("Enter the developer nickname in Github: ")
    developer = search_developer(username)
    print(developer)    

if __name__ == "__main__":
    main()