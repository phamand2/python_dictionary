# Write a function that called most_characters that accepts a string, and return the character that appears the most.

def most_characters(check_string):
  

  count = {}

  for s in check_string.lower():
    if s in count:
      count[s] += 1
    else:
      count[s] = 1
      

  # Iterate through the 'count' dictionary
  for key in count:
    # If a key is repeated more than 1 times
    if count[key] > 1:
      # print the key and number
      print (key,':', count[key])


most_characters('aaabbbc')