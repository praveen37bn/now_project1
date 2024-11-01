import requests
import csv
import time

# GitHub API token
GITHUB_TOKEN = 'Replace with your actual GitHub token'  # Replace with your actual GitHub token
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# Helper function to clean up company names
def clean_company_name(company):
    if company:
        company = company.strip().lstrip('@').upper()
    return company or ""

# Function to fetch users from the GitHub API
def fetch_users(city="Sydney", min_followers=100):
    users = []
    page = 1

    while True:
        url = f"https://api.github.com/search/users?q=location:{city}+followers:>{min_followers}&page={page}&per_page=100"
        response = requests.get(url, headers=HEADERS)
        
        # Handle rate limits and errors
        if response.status_code == 403:
            print("Rate limit reached, waiting for reset...")
            time.sleep(60)
            continue

        data = response.json()

        # Break if no more results
        if 'items' not in data or not data['items']:
            break

        for user in data['items']:
            user_url = user['url']
            user_response = requests.get(user_url, headers=HEADERS)
            user_data = user_response.json()

            # Extract required fields with cleaned data
            users.append({
                'login': user_data.get('login', ""),
                'name': user_data.get('name', ""),
                'company': clean_company_name(user_data.get('company')),
                'location': user_data.get('location', ""),
                'email': user_data.get('email', "") if user_data.get('email') else "",
                'hireable': 'true' if user_data.get('hireable') else 'false' if user_data.get('hireable') is not None else "",
                'bio': user_data.get('bio', "") if user_data.get('bio') else "",
                'public_repos': user_data.get('public_repos', 0),
                'followers': user_data.get('followers', 0),
                'following': user_data.get('following', 0),
                'created_at': user_data.get('created_at', "")
            })

            # Delay to avoid hitting API limits
            time.sleep(1)

        page += 1
        time.sleep(1)  # Pause to avoid hitting API rate limits

    return users

# Function to fetch repositories for a user
def fetch_repositories(user_login):
    repositories = []
    page = 1

    while True:
        url = f"https://api.github.com/users/{user_login}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=HEADERS)

        # Handle rate limits and errors
        if response.status_code == 403:
            print("Rate limit reached, waiting for reset...")
            time.sleep(60)
            continue

        repo_data = response.json()

        # Break if no more repositories
        if not repo_data:
            break

        for repo in repo_data:
            repositories.append({
                'login': user_login,
                'full_name': repo.get('full_name', ""),
                'created_at': repo.get('created_at', ""),
                'stargazers_count': repo.get('stargazers_count', 0),
                'watchers_count': repo.get('watchers_count', 0),
                'language': repo.get('language', ""),
                'has_projects': 'true' if repo.get('has_projects') else 'false',
                'has_wiki': 'true' if repo.get('has_wiki') else 'false',
                'license_name': repo['license']['key'] if repo.get('license') else ""
            })

        if len(repo_data) < 100:
            break

        page += 1
        time.sleep(1)  # Pause to avoid hitting API rate limits

    return repositories

# Save users to CSV
def save_users_to_csv(users, filename="users.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=users[0].keys())
        writer.writeheader()
        writer.writerows(users)

# Save repositories to CSV
def save_repositories_to_csv(repositories, filename="repositories.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=repositories[0].keys())
        writer.writeheader()
        writer.writerows(repositories)

# Main function to run the script
def main():
    print("Fetching users...")
    users = fetch_users(city="Sydney", min_followers=100)
    save_users_to_csv(users)
    print(f"Saved {len(users)} users to users.csv")

    print("Fetching repositories...")
    all_repositories = []
    for user in users:
        user_repos = fetch_repositories(user["login"])
        all_repositories.extend(user_repos)
        print(f"Fetched {len(user_repos)} repositories for user {user['login']}")

    save_repositories_to_csv(all_repositories)
    print(f"Saved {len(all_repositories)} repositories to repositories.csv")

if __name__ == "__main__":
    main()
