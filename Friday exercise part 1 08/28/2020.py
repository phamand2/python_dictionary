#Write a function that accepts two lists
def has_same_digit_frequency(list1, list2):
  list1.sort()
  list2.sort()
  # Create a variable called 'result' and assign it to an empty dictionary
  result = False
  # Use a for loop to compare the two list
  for num in list1:
    # Add another inner loop for the second argument
    for num2 in list2:
      # Use an operator to check if the two list has matching numbers
      if num == num2:
        result = True
        return result



# def has_same_digit_frequency(a,b):
#   if len(a) != len(b):
#     return False

#   result = {}

#   for number in a:
#     if number in result.keys():
#       result[number] += 1
#     else:
#       result[number] = 1


#   print(result)



print(has_same_digit_frequency([1,2,4,5], [5,5,5,5]))