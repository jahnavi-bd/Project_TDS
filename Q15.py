import pandas as pd

# Load the users data
users_df = pd.read_csv('users.csv')

# Convert "true"/"false" to actual booleans
users_df['hireable'] = users_df['hireable'].replace({'true': True, 'false': False, '': None})

# Calculate fraction of users with email when hireable is True
fraction_email_hireable = users_df[users_df['hireable'] == True]['email'].notnull().mean()

# Calculate fraction of users with email when hireable is False
fraction_email_non_hireable = users_df[users_df['hireable'] == False]['email'].notnull().mean()

# Calculate the difference
email_fraction_difference = round(fraction_email_hireable - fraction_email_non_hireable, 3)

print(f"Email sharing difference: {email_fraction_difference}")
