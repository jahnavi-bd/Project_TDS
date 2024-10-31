import pandas as pd

# Load the saved repositories CSV file
repos_df = pd.read_csv('repositories.csv')

# Remove rows where 'language' is empty or NaN
repos_df = repos_df[repos_df['language'].notnull() & (repos_df['language'] != '')]

# Group by language and calculate the average number of stars
average_stars = repos_df.groupby('language')['stargazers_count'].mean()

# Find the language with the highest average stars
highest_average_language = average_stars.idxmax()
highest_average_value = average_stars.max()

# Output the result
print(f"Language with the highest average number of stars per repository: {highest_average_language} ({highest_average_value:.2f} stars)")
