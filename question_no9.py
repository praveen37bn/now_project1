import csv
import numpy as np

# Function to load users from CSV
def load_users_from_csv(filename="users.csv"):
    followers = []
    public_repos = []
    
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert relevant fields to integers
            if row['followers'].isdigit() and row['public_repos'].isdigit():
                followers.append(int(row['followers']))
                public_repos.append(int(row['public_repos']))
    
    return followers, public_repos

# Function to calculate correlation
def calculate_correlation(followers, public_repos):
    if len(followers) == 0 or len(public_repos) == 0:
        return None
    correlation = np.corrcoef(followers, public_repos)[0, 1]
    return correlation

# Main function to run the script
def main():
    followers, public_repos = load_users_from_csv()
    correlation = calculate_correlation(followers, public_repos)
    
    if correlation is not None:
        print(f"Correlation between followers and public repositories: {correlation:.3f}")
    else:
        print("Insufficient data to calculate correlation.")

if __name__ == "__main__":
    main()
