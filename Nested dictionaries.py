ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# Write a python expression that gets the email address of Ramit.
print(f'Ramit email is {ramit.get("email")}.''\n')

# Write a python expression that gets the first of Ramit's interests.
print(f'Ramit first interest is {ramit.get("interests")[0]}.''\n')

# Write a python expression that gets the email address of Jasmine.
jasmine_email = ramit['friends'][0]
print(f'Jasmine email is {jasmine_email["email"]}.''\n')

# Write a python expression that gets the second of Jan's two interests

jan_two_interests = ramit['friends'][1]
print(f'Jan two interests are {jan_two_interests["interests"][0]} and {jan_two_interests["interests"][1]}.''\n')