import requests
import pandas as pd
import time

# Prompt the user for their personal access token
ACCESS_TOKEN = input("Please enter your GitHub personal access token: ")

def check_rate_limit():
    headers = {'Authorization': f'token {ACCESS_TOKEN}'}
    response = requests.get("https://api.github.com/rate_limit", headers=headers)
    return response.json()

def fetch_users(location="Melbourne", min_followers=100):
    users = []
    page = 1

    while True:
        url = f"https://api.github.com/search/users?q=location:{location}+followers:>{min_followers}&per_page=100&page={page}"
        headers = {'Authorization': f'token {ACCESS_TOKEN}'}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Error fetching users: {response.json()}")
            break

        data = response.json()
        users.extend(data.get("items", []))

        if len(data.get("items", [])) < 100:
            break
        
        page += 1
        time.sleep(1)

    return users

def fetch_user_details(user):
    url = f"https://api.github.com/users/{user['login']}"
    headers = {'Authorization': f'token {ACCESS_TOKEN}'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error fetching user details for {user['login']}: {response.json()}")
        return {}

    return response.json()

def fetch_repositories(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    headers = {'Authorization': f'token {ACCESS_TOKEN}'}
    all_repos = []
    
    while True:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            repos = response.json()
            all_repos.extend(repos)
            if len(repos) < 100 or len(all_repos) >= 500:
                break
        elif response.status_code == 403:  # Rate limit exceeded
            print("Rate limit exceeded. Waiting for reset...")
            time.sleep(60)
        else:
            print(f"Error fetching repositories for {username}: {response.json()}")
            return []

        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={len(all_repos) // 100 + 1}"
    
    return all_repos[:500]  # Limit to 500 repositories

# Fetch users and their details
users = fetch_users()
user_details = []

for user in users:
    details = fetch_user_details(user)
    if details:
        user_details.append({
            'login': details.get('login', ''),
            'name': details.get('name', ''),
            'company': (details.get('company', '') or '').strip('@').strip().upper(),
            'location': details.get('location', ''),
            'email': details.get('email', '') or '',
            'hireable': 'true' if details.get('hireable') else 'false',
            'bio': details.get('bio', ''),
            'public_repos': details.get('public_repos', ''),
            'followers': details.get('followers', ''),
            'following': details.get('following', ''),
            'created_at': details.get('created_at', ''),
        })
    time.sleep(1)

# Fetch repositories
all_repositories = []

for user in user_details:
    repos = fetch_repositories(user['login'])
    for repo in repos:
        all_repositories.append({
            'login': user['login'],
            'full_name': repo['full_name'],
            'created_at': repo['created_at'],
            'stargazers_count': repo['stargazers_count'],
            'watchers_count': repo['watchers_count'],
            'language': repo['language'] or '',
            'has_projects': 'true' if repo.get('has_projects') else 'false',
            'has_wiki': 'true' if repo.get('has_wiki') else 'false',
            'license_name': repo['license']['name'] if repo.get('license') else ''
        })
    time.sleep(1)

# Save users to CSV
users_df = pd.DataFrame(user_details)
users_df.to_csv('users.csv', index=False)

# Save repositories to CSV
repos_df = pd.DataFrame(all_repositories)
repos_df.to_csv('repositories.csv', index=False)
