import csv

# Function to load users from CSV
def load_users_from_csv(filename="users.csv"):
    hireable_following = []
    non_hireable_following = []
    
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            following = int(row['following'])  # Convert following to int
            if row['hireable'].lower() == 'true':
                hireable_following.append(following)
            else:
                non_hireable_following.append(following)
    
    return hireable_following, non_hireable_following

# Function to calculate average
def calculate_average(following_list):
    if following_list:  # Avoid division by zero
        return sum(following_list) / len(following_list)
    return 0  # Return 0 if list is empty

# Main function to run the script
def main():
    hireable_following, non_hireable_following = load_users_from_csv()
    
    # Calculate averages
    average_hireable = calculate_average(hireable_following)
    average_non_hireable = calculate_average(non_hireable_following)
    
    # Calculate the difference
    difference = average_hireable - average_non_hireable
    
    print(f"Average following per user for hireable=true minus the average following for the rest: {difference:.3f}")

if __name__ == "__main__":
    main()
