import csv
import numpy as np

# Function to load repositories from CSV
def load_repositories_from_csv(filename="repositories.csv"):
    has_projects = []
    has_wiki = []
    
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert 'has_projects' and 'has_wiki' to boolean values
            has_projects.append(1 if row['has_projects'].lower() == 'true' else 0)  # Convert to 1 or 0
            has_wiki.append(1 if row['has_wiki'].lower() == 'true' else 0)          # Convert to 1 or 0
    
    return has_projects, has_wiki

# Function to calculate the correlation
def calculate_correlation(has_projects, has_wiki):
    correlation = np.corrcoef(has_projects, has_wiki)[0, 1]  # Correlation coefficient
    return correlation

# Main function to run the script
def main():
    has_projects, has_wiki = load_repositories_from_csv()
    correlation = calculate_correlation(has_projects, has_wiki)
    
    print(f"Correlation between projects enabled and wiki enabled: {correlation:.3f}")

if __name__ == "__main__":
    main()
