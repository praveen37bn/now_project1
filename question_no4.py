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

# Function to clean and count companies
def get_most_common_company(users):
    company_counter = Counter()

    for user in users:
        company = user['company']
        if company:  # Only process if company is not empty
            # Clean up the company name
            cleaned_company = company.strip().lstrip('@').upper()
            company_counter[cleaned_company] += 1

    # Get the most common company
    most_common_company = company_counter.most_common(1)
    return most_common_company[0][0] if most_common_company else None

# Main function to run the script
def main():
    users = load_users_from_csv()
    most_common_company = get_most_common_company(users)

    print("The company that the majority of these developers work at is:", most_common_company)

if __name__ == "__main__":
    main()
