import pandas as pd

# Load the users CSV file
users_df = pd.read_csv('users.csv')

# Calculate leader_strength
users_df['leader_strength'] = users_df['followers'] / (1 + users_df['following'])

# Get the top 5 users based on leader_strength
top_leaders = users_df.nlargest(5, 'leader_strength')

# Extract the logins and format as a comma-separated string
top_leader_logins = ', '.join(top_leaders['login'].tolist())

# Output the result
print(f"Top 5 users in terms of leader_strength: {top_leader_logins}")
