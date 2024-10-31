import csv
from collections import defaultdict
from datetime import datetime

# Function to load repositories from CSV and filter by weekend
def load_repositories_from_csv(filename="repositories.csv"):
    weekend_users = defaultdict(int)  # Dictionary to count repositories per user
    
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            created_at = row['created_at']
            login = row['login']
            
            # Parse the created_at date
            created_date = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")  # UTC
            
            # Check if the created day is Saturday (5) or Sunday (6)
            if created_date.weekday() in [5, 6]:
                weekend_users[login] += 1  # Increment the count for the user
    
    return weekend_users

# Function to get top 5 users who created the most repositories on weekends
def get_top_weekend_users(weekend_users):
    # Sort users by the number of repositories created on weekends
    sorted_users = sorted(weekend_users.items(), key=lambda x: x[1], reverse=True)
    
    return [user[0] for user in sorted_users[:5]]  # Get top 5 user logins

# Main function to run the script
def main():
    weekend_users = load_repositories_from_csv()
    top_users = get_top_weekend_users(weekend_users)
    
    print("Top 5 users who created the most repositories on weekends:")
    print(", ".join(top_users))

if __name__ == "__main__":
    main()
