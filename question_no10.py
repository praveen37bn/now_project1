import csv
import numpy as np
import statsmodels.api as sm

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

# Function to perform linear regression and get the slope
def calculate_regression_slope(followers, public_repos):
    X = sm.add_constant(public_repos)  # Adds a constant term to the predictor
    model = sm.OLS(followers, X).fit()  # Fit the model
    slope = model.params[1]  # Get the slope for public_repos
    return slope

# Main function to run the script
def main():
    followers, public_repos = load_users_from_csv()
    slope = calculate_regression_slope(followers, public_repos)
    
    print(f"Regression slope of followers on public repositories: {slope:.3f}")

if __name__ == "__main__":
    main()

