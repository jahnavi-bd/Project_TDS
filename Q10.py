import pandas as pd
import statsmodels.api as sm

# Load your users DataFrame (assuming it's already created)
users_df = pd.read_csv('users.csv')

# Ensure relevant columns are numeric
users_df['public_repos'] = users_df['public_repos'].astype(float)
users_df['followers'] = users_df['followers'].astype(float)

# Drop rows with NaN values in relevant columns
users_df = users_df.dropna(subset=['public_repos', 'followers'])

# Define the independent (X) and dependent (y) variables
X = users_df['public_repos']
y = users_df['followers']

# Add a constant to the independent variable (for the intercept)
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Get the slope (coefficient of public_repos)
slope = model.params['public_repos']

print(f"Regression slope of followers on repos: {slope}")
