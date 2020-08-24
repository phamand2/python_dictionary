phonebook_dict = {
    'Alice' : '703-493-1834',
    'Bob' : '857-384-1234',
    'Elizabeth' : '484-584-2923'
}

counter = 0

while counter < 5:
    if counter == 0:
      # Print Elizabeth phone number
        print(f'Elizabeth\'s phone number is: {phonebook_dict["Elizabeth"]}')
    elif counter == 1: 
        # A Add an entry to the dictionary: Kareem's number is 938-489-1234
        phonebook_dict.update({'Kareem' : '938-489-1234'})
    elif counter == 2:
        # Delete Alice's phone entry
        del phonebook_dict["Alice"]
    elif counter == 3:
        # Change Bob's phone number to '968-345-2345
        phonebook_dict["Bob"] = '968-345-2345'
    elif counter == 4:
        
        # Print all the phone entries with a for loop
        for key in phonebook_dict.keys():
            print(f'{key}: {phonebook_dict[key]}')
    counter += 1