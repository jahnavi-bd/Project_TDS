import pandas as pd

# Load repositories from CSV
repos_df = pd.read_csv('repositories.csv')

# Convert created_at to datetime
repos_df['created_at'] = pd.to_datetime(repos_df['created_at'])

# Extract day of the week (0 = Monday, ..., 6 = Sunday)
repos_df['day_of_week'] = repos_df['created_at'].dt.dayofweek

# Filter for weekend days (Saturday and Sunday)
weekend_repos = repos_df[repos_df['day_of_week'].isin([5, 6])]

# Count repositories created by each user
weekend_counts = weekend_repos['login'].value_counts()

# Get the top 5 users
top_weekend_users = weekend_counts.head(5).index.tolist()

# Format the result as a comma-separated string
result = ', '.join(top_weekend_users)

print(f"Top 5 users with the most repositories created on weekends: {result}")
