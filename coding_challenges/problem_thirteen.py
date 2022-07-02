# *Problem 13*. Write a function that takes 2 lists, and return their intersection.

def intersection(list1, list2):
    return [i for i in list1 if i in list2]

list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list2 = ['12', '32', '3', '64', '56',]

print("Intersection:", intersection(list1, list2))