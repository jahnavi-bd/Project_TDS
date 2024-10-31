# Sort users by the 'created_at' date and get the top 5 earliest registered users
earliest_users = sorted(user_details, key=lambda x: x['created_at'])[:5]
earliest_user_logins = [user['login'] for user in earliest_users]

# Output the logins in ascending order without space after the comma
print("Earliest registered users: " + ",".join(earliest_user_logins))