# *Problem 15*:
# Write a dictionary which takes strings as their keys from user input (using the “input” function), 
# and makes the value the number of times the user has inputted that thing. So, if the user inputs ‘a’, then ‘b‘, and then ’a’, 
# the dictionary should be {’a’: 2, ’b’: 1}.

keys = input('Enter a string: ')

dictionary = {}

for key in keys:
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1

for key, value in dictionary.items():
    print(f'{key}: {value}')
