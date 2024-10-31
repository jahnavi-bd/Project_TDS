import pandas as pd

# Load the users data
users_df = pd.read_csv('users.csv')
# Remove users without bios
users_df = users_df[users_df['bio'].notna()]

# Calculate the length of each bio in words (Unicode words, split by whitespace)
users_df['bio_word_count'] = users_df['bio'].str.split().str.len()
import statsmodels.api as sm

# Define the independent variable (bio word count) and dependent variable (followers)
X = users_df['bio_word_count']
y = users_df['followers']

# Add a constant to the independent variable
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Get the regression results
slope = model.params['bio_word_count']
print(f'Regression slope of followers on bio word count: {slope:.3f}')
