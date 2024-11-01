import csv

# Function to load users from CSV
def load_users_from_csv(filename="users.csv"):
    users = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

# Function to calculate the difference in email sharing between hireable and non-hireable users
def calculate_email_sharing_difference(users):
    hireable_with_email = 0
    hireable_count = 0
    non_hireable_with_email = 0
    non_hireable_count = 0

    for user in users:
        is_hireable = user.get('hireable', 'false').lower() == 'true'  # Check if hireable
        email = user.get('email', '').strip()  # Get email

        if is_hireable:
            hireable_count += 1
            if email:  # If email exists
                hireable_with_email += 1
        else:
            non_hireable_count += 1
            if email:  # If email exists
                non_hireable_with_email += 1

    # Calculate fractions
    hireable_fraction = hireable_with_email / hireable_count if hireable_count > 0 else 0
    non_hireable_fraction = non_hireable_with_email / non_hireable_count if non_hireable_count > 0 else 0

    # Calculate the difference
    difference = hireable_fraction - non_hireable_fraction

    return round(difference, 3)  # Return the difference rounded to 3 decimal places

# Main function to run the script
def main():
    users = load_users_from_csv()
    difference = calculate_email_sharing_difference(users)

    # Print the difference
    print(f"Difference in email sharing: {difference:.3f}")

if __name__ == "__main__":
    main()
