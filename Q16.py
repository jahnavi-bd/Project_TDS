import pandas as pd
from collections import Counter

# Load the users data
users_df = pd.read_csv('users.csv')

# Function to extract surnames
def get_surname(name):
    if pd.isna(name) or not name.strip():
        return None
    # Split by whitespace and return the last element
    return name.strip().split()[-1]

# Apply the function to extract surnames
users_df['surname'] = users_df['name'].apply(get_surname)

# Drop rows with NaN surnames
surnames = users_df['surname'].dropna()

# Count occurrences of each surname
surname_counts = Counter(surnames)

# Maximum count
max_count = max(surname_counts.values())

# Surnames that have the maximum count
most_common_surnames = sorted([surname for surname, count in surname_counts.items() if count == max_count])
print(most_common_surnames[-1])
