import pandas as pd
from collections import Counter

# Load users from CSV
users_df = pd.read_csv('users.csv')

# Load repositories from CSV
repos_df = pd.read_csv('repositories.csv')

# Convert 'created_at' to datetime
users_df['created_at'] = pd.to_datetime(users_df['created_at'])

# Filter users who joined after 2020
recent_users = users_df[users_df['created_at'] > '2020-01-01']

# Get logins of recent users
recent_user_logins = recent_users['login'].tolist()

# Filter repositories by recent users
recent_repos = repos_df[repos_df['login'].isin(recent_user_logins)]

# Count occurrences of each programming language
language_counts = Counter(recent_repos['language'].dropna())

# Get the second most common language
most_common_languages = language_counts.most_common(2)
second_most_popular_language = most_common_languages[1][0] if len(most_common_languages) > 1 else None

# Output the second most popular language
print("Second most popular language:", second_most_popular_language)
