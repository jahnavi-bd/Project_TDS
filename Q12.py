import pandas as pd

# Load the users data
users_df = pd.read_csv('users.csv')

# Convert "true"/"false" to actual booleans
users_df['hireable'] = users_df['hireable'].replace({'true': True, 'false': False, '': None})
users_df['following'] = pd.to_numeric(users_df['following'], errors='coerce')

# Calculate average following for hireable and non-hireable users
avg_following_hireable = users_df[users_df['hireable'] == True]['following'].mean()
avg_following_non_hireable = users_df[users_df['hireable'] == False]['following'].mean()

# Calculate the difference
following_difference = round(avg_following_hireable - avg_following_non_hireable, 3)

print(f"Average following difference: {following_difference}")
