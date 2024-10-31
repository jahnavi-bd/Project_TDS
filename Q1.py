import pandas as pd

# Load the users CSV file
users_df = pd.read_csv('users.csv')

# Sort users by the 'followers' column in descending order and get the top 5
top_users = users_df.nlargest(5, 'followers')

# Extract the logins and format as a comma-separated string without spaces
top_user_logins = ','.join(top_users['login'].tolist())

# Output the result
print(f"Top 5 users in Melbourne by followers: {top_user_logins}")
