import pandas as pd
# Sort users by the number of followers and get the top 5 users
top_users = sorted(user_details, key=lambda x: x['followers'], reverse=True)[:5]
top_user_logins = [user['login'] for user in top_users]

# Output the logins in order without space after the comma
print("Top 5 users in Melbourne: " + ",".join(top_user_logins))
