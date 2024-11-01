import csv
from collections import Counter

# Function to load repositories from CSV
def load_repositories_from_csv(filename="repositories.csv"):
    repositories = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            repositories.append(row)
    return repositories

# Function to get the most common licenses
def get_most_common_licenses(repositories, top_n=3):
    license_counter = Counter()

    for repo in repositories:
        license_name = repo['license_name']
        if license_name:  # Ignore missing licenses
            license_counter[license_name] += 1

    # Get the most common licenses
    most_common_licenses = license_counter.most_common(top_n)
    return [license[0] for license in most_common_licenses]

# Main function to run the script
def main():
    repositories = load_repositories_from_csv()
    most_common_licenses = get_most_common_licenses(repositories)

    print("The 3 most popular licenses are:", ", ".join(most_common_licenses))

if __name__ == "__main__":
    main()
