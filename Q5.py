import pandas as pd

# Load the saved CSV files
users_df = pd.read_csv('users.csv')
repos_df = pd.read_csv('repositories.csv')

# Convert the created_at column to datetime
users_df['created_at'] = pd.to_datetime(users_df['created_at'])

# Filter users who joined after January 1, 2021
filtered_users = users_df[users_df['created_at'] > '2021-01-01']

# Gather languages from repositories of these users
language_counts = repos_df[repos_df['login'].isin(filtered_users['login'])]['language'].value_counts()

# Identify the second most popular language
most_common_languages = language_counts.nlargest(2)

if len(most_common_languages) > 1:
    second_most_popular_language = most_common_languages.index[1]  # Get the second one
else:
    second_most_popular_language = None

# Output the second most popular language
if second_most_popular_language:
    print("Second most popular programming language:", second_most_popular_language)
else:
    print("No second most popular language found.")
