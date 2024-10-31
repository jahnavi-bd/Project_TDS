import pandas as pd

# Load the users CSV file
users_df = pd.read_csv('users.csv')

# Convert the 'created_at' column to datetime
users_df['created_at'] = pd.to_datetime(users_df['created_at'])

# Sort users by the 'created_at' date in ascending order and get the top 5
earliest_users = users_df.nsmallest(5, 'created_at')

# Extract the logins and format as a comma-separated string without spaces
earliest_user_logins = ','.join(earliest_users['login'].tolist())

# Output the result
print(f"Earliest registered users in Melbourne: {earliest_user_logins}")
