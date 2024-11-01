import csv
from datetime import datetime

def load_users_from_csv(filename):
    users = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

def find_earliest_users(users, count=5):
    # Convert the created_at string to datetime objects for sorting
    for user in users:
        user['created_at'] = datetime.strptime(user['created_at'], "%Y-%m-%dT%H:%M:%SZ")
    
    # Sort users by created_at date
    users.sort(key=lambda x: x['created_at'])

    # Get the top 'count' earliest users
    earliest_users = users[:count]
    return [user['login'] for user in earliest_users]

def main():
    users = load_users_from_csv("users.csv")
    earliest_users = find_earliest_users(users)
    print(", ".join(earliest_users))

if __name__ == "__main__":
    main()
