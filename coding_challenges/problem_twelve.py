# *Problem 12*. Write a function that takes two lists and returns the values that are not in the second list, stored in a new list.

def ListUnions(list1, list2):
    list3 = [i for i in list1 if i not in list2]
    return list3


list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list2 = ['12', '32', '3', '64', '5',]

# print list
print("New list", ListUnions(list1, list2))