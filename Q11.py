import pandas as pd

# Load repositories from CSV
repos_df = pd.read_csv('repositories.csv')

# Convert string representations of booleans to actual booleans
repos_df['has_projects'] = repos_df['has_projects'].replace({'true': True, 'false': False, '': None})
repos_df['has_wiki'] = repos_df['has_wiki'].replace({'true': True, 'false': False, '': None})

# Drop rows where either has_projects or has_wiki is NaN
filtered_df = repos_df.dropna(subset=['has_projects', 'has_wiki'])

# Calculate correlation
correlation = filtered_df['has_projects'].astype(int).corr(filtered_df['has_wiki'].astype(int))

# Print the result rounded to three decimal places
print(f"{correlation:.3f}")
