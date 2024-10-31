import pandas as pd
from collections import Counter

# Load repositories from CSV
repos_df = pd.read_csv('repositories.csv')

# Count occurrences of each license, ignoring missing licenses
license_counts = Counter(repo.license_name for repo in repos_df.itertuples() if isinstance(repo.license_name, str) and repo.license_name)

# Get the 3 most common licenses
most_common_licenses = license_counts.most_common(3)
popular_licenses = [license[0] for license in most_common_licenses]

# Format the result as a comma-separated string without spaces
result = ','.join(filter(lambda x: isinstance(x, str), popular_licenses))

# Output the result
print(f"Most popular licenses: {result}")
