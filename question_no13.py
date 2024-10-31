import csv
import numpy as np
from sklearn.linear_model import LinearRegression

# Function to load users from CSV
def load_users_from_csv(filename="users.csv"):
    users = []
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

# Function to calculate the regression slope
def calculate_regression_slope(users):
    bio_word_counts = []
    follower_counts = []

    for user in users:
        bio = user.get('bio', '').strip()
        followers = int(user.get('followers', 0))  # Assuming followers is an integer

        if bio:  # Only consider users with a bio
            word_count = len(bio.split())
            bio_word_counts.append(word_count)
            follower_counts.append(followers)

    # Convert lists to numpy arrays for regression
    X = np.array(bio_word_counts).reshape(-1, 1)  # Features (bio word counts)
    y = np.array(follower_counts)  # Target (follower counts)

    # Perform linear regression
    model = LinearRegression()
    model.fit(X, y)

    return model.coef_[0]  # Return the slope

# Main function to run the script
def main():
    users = load_users_from_csv()
    slope = calculate_regression_slope(users)

    # Print the slope rounded to 3 decimal places
    print(f"Regression slope of followers on bio word count: {slope:.3f}")

if __name__ == "__main__":
    main()
