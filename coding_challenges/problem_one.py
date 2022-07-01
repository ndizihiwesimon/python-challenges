# Integer List
IntegerList = [2,4,11,23,1,0,5]

# Setting initial values for the Smallest and largest values
smallest = largest = IntegerList[0]

# For loop comparing the smallest and largest values
for a in range(1, len(IntegerList)):
    if(smallest > IntegerList[a]):
        smallest = IntegerList[a]
    if(largest < IntegerList[a]):
        largest = IntegerList[a]

# Printing the results
print("The Smallest Element in this List is : ", smallest)
print("The Largest Element in this List is : ", largest)
