
def countFriends(dictionary):
  count = 0
  if 'friends' in dictionary.keys():
    for friend in dictionary['friends']:
      count += 1
  dictionary['friends-count'] = count    
  return dictionary


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

print(countFriends(ramit))
