import pandas as pd

# Load users from CSV
users_df = pd.read_csv('users.csv')

# Filter for users in Melbourne
melbourne_users = users_df[users_df['location'].str.contains('Melbourne', case=False, na=False)]

# Convert followers to numeric
melbourne_users['followers'] = pd.to_numeric(melbourne_users['followers'], errors='coerce')

# Get the top 5 users with the highest followers
top_users = melbourne_users.nlargest(5, 'followers')

# Extract their logins and format as a comma-separated string
top_user_logins = ', '.join(top_users['login'].tolist())

print(f"Top 5 users in Melbourne by followers: {top_user_logins}")