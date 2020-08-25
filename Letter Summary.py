def char_frequency(word):
    dict = {}
    for letter in word:
        keys = dict.keys()
        if letter in keys:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict


user_input = input('Please enter a word: ')

print(char_frequency(user_input))

