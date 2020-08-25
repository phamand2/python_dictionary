def word_count(word):
    dict = {}
    words = word.split()
    

    for word in words:
      counts = dict.keys()
      if word in counts:
          dict[word] += 1
      else:
          dict[word] = 1

    return dict


user_input = input('Please enter a phrase: ')

print(word_count(user_input))    