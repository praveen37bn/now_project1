import csv
from collections import Counter
from datetime import datetime

# Function to load users from CSV
def load_users_from_csv(filename="users.csv"):
    users = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

# Function to load repositories from CSV
def load_repositories_from_csv(filename="repositories.csv"):
    repositories = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            repositories.append(row)
    return repositories

# Function to get the counts of all programming languages among users who joined after 2020
def get_all_languages_count(users, repositories):
    language_counter = Counter()
    cutoff_date = datetime(2020, 12, 31)  # Cutoff for users who joined after 2020

    # Filter users who joined after December 31, 2020
    filtered_users = [
        user for user in users
        if datetime.strptime(user['created_at'], '%Y-%m-%dT%H:%M:%SZ') > cutoff_date
    ]
    
    # Create a set of logins for the filtered users
    filtered_logins = {user['login'] for user in filtered_users}

    # Count languages for the filtered users' repositories
    for repo in repositories:
        if repo['login'] in filtered_logins and repo['language']:
            language_counter[repo['language']] += 1

    return language_counter  # Return all languages and their counts

# Main function to run the script
def main():
    users = load_users_from_csv()
    repositories = load_repositories_from_csv()
    language_counts = get_all_languages_count(users, repositories)

    if language_counts:
        # Sort languages by count in descending order
        sorted_language_counts = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)
        
        print("Programming languages and their counts among users who joined after 2020:")
        for language, count in sorted_language_counts:
            print(f"{language}: {count}")
    else:
        print("No data available for users who joined after 2020.")

if __name__ == "__main__":
    main()
