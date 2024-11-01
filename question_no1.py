import csv

# Load the users from the CSV file
def load_users_from_csv(filename="users.csv"):
    users = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert followers to int for sorting
            row['followers'] = int(row['followers'])
            users.append(row)
    return users

# Find the top 5 users by followers
def top_5_users_by_followers(users):
    sorted_users = sorted(users, key=lambda x: x['followers'], reverse=True)
    top_users = sorted_users[:5]
    return [user['login'] for user in top_users]

# Main execution
if __name__ == "__main__":
    users = load_users_from_csv()
    top_users = top_5_users_by_followers(users)
    print("Top 5 users in Sydney with the highest number of followers:")
    print(", ".join(top_users))
