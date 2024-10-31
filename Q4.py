from collections import Counter

# Count occurrences of each company, ignoring empty strings
company_counts = Counter(user['company'] for user in user_details if user['company'])

# Get the most common company
most_common_company = company_counts.most_common(1)

# Output the company name
if most_common_company:
    print("Most common company:", most_common_company[0][0])
else:
    print("No company data available.")
