import pandas as pd
from collections import Counter

# Count occurrences of each license, ignoring missing licenses
license_counts = Counter(repo['license_name'] for repo in all_repositories if repo['license_name'])

# Get the 3 most common licenses
most_common_licenses = license_counts.most_common(3)
popular_licenses = [license[0] for license in most_common_licenses]

# Output the licenses in order without space after the comma
print("Most popular licenses: " + ",".join(popular_licenses))
