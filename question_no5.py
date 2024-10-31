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

# Function to get the most popular programming language
def get_most_popular_language(repositories):
    language_counter = Counter()

    for repo in repositories:
        language = repo['language']
        if language:  # Only process if language is not empty
            language_counter[language] += 1

    # Get the most common language
    most_common_language = language_counter.most_common(1)
    return most_common_language[0][0] if most_common_language else None

# Main function to run the script
def main():
    repositories = load_repositories_from_csv()
    most_popular_language = get_most_popular_language(repositories)

    print("The most popular programming language among these users is:", most_popular_language)

if __name__ == "__main__":
    main()
