import csv

# Function to load users from CSV
def load_users_from_csv(filename="users.csv"):
    users = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert relevant fields to integers for calculations
            row['followers'] = int(row['followers']) if row['followers'].isdigit() else 0
            row['following'] = int(row['following']) if row['following'].isdigit() else 0
            users.append(row)
    return users

# Function to calculate leader strength
def calculate_leader_strength(users):
    for user in users:
        following_count = user['following']
        user['leader_strength'] = user['followers'] / (1 + following_count) if following_count >= 0 else 0

    # Sort users by leader_strength in descending order
    sorted_users = sorted(users, key=lambda x: x['leader_strength'], reverse=True)
    return sorted_users

# Main function to run the script
def main():
    users = load_users_from_csv()
    sorted_users = calculate_leader_strength(users)

    # Get the top 5 users by leader_strength
    top_5_users = sorted_users[:5]
    top_5_logins = [user['login'] for user in top_5_users]

    print("Top 5 users in terms of leader_strength:", ", ".join(top_5_logins))

if __name__ == "__main__":
    main()
