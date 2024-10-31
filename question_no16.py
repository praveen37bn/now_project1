import csv
from collections import Counter

# Function to load users from CSV
def load_users_from_csv(filename="users.csv"):
    users = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

# Function to find the most common surname
def find_most_common_surname(users):
    surnames = []

    for user in users:
        full_name = user.get('name', '').strip()  # Get the user's name
        if full_name:  # Ignore missing names
            # Split the name and take the last part as the surname
            surname = full_name.split()[-1]  
            surnames.append(surname)

    # Count occurrences of each surname
    surname_counts = Counter(surnames)
    
    # Find the most common surname and its count
    if surname_counts:
        most_common_surname, count = surname_counts.most_common(1)[0]
        return most_common_surname, count
    else:
        return None, 0

def main():
    # Load users from CSV file
    users = load_users_from_csv("users.csv")
    
    # Find the most common surname
    most_common_surname, count = find_most_common_surname(users)

    if most_common_surname:
        print(f"The most common surname is '{most_common_surname}' with {count} users.")
    else:
        print("No surnames found.")

if __name__ == "__main__":
    main()
