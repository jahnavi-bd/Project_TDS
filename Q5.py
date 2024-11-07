from collections import Counter

# Function to calculate the most popular programming language
def most_popular_language(repositories):
    # Extract all the programming languages from the repositories
    languages = [repo['language'] for repo in repositories if repo['language']]
    
    # Use Counter to find the most common language
    language_count = Counter(languages)
    
    # Get the most common language
    most_common_language = language_count.most_common(1)
    
    if most_common_language:
        return most_common_language[0]  # (language, count)
    else:
        return None

# Get the most popular programming language
popular_language = most_popular_language(all_repositories)

# Display the result
if popular_language:
    print(f"The most popular programming language among these users is: {popular_language[0]}")
else:
    print("No repositories with specified languages were found.")
