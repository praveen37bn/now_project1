import csv
from collections import defaultdict

# Function to load repositories from CSV
def load_repositories_from_csv(filename="repositories.csv"):
    repositories = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            repositories.append(row)
    return repositories

# Function to get the language with the highest average number of stars per repository
def get_language_with_highest_average_stars(repositories):
    language_stars = defaultdict(list)

    # Group repositories by language and collect their star counts
    for repo in repositories:
        if repo['language'] and repo['stargazers_count'].isdigit():
            language_stars[repo['language']].append(int(repo['stargazers_count']))

    # Calculate the average stars per repository for each language
    language_averages = {}
    for language, stars in language_stars.items():
        average_stars = sum(stars) / len(stars)
        language_averages[language] = average_stars

    # Determine the language with the highest average
    if language_averages:
        highest_average_language = max(language_averages, key=language_averages.get)
        return highest_average_language, language_averages[highest_average_language]
    else:
        return None, None  # Not enough data

# Main function to run the script
def main():
    repositories = load_repositories_from_csv()
    highest_average_language, average_stars = get_language_with_highest_average_stars(repositories)

    if highest_average_language:
        print(f"The programming language with the highest average number of stars per repository is: {highest_average_language} (Average: {average_stars:.2f} stars)")
    else:
        print("Not enough data to determine the language with the highest average stars.")

if __name__ == "__main__":
    main()
