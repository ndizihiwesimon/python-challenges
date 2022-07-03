# *Problem 18*. Write a function of your choosing which takes and returns a number (such as def double(x): return x*2). 
# Write another function which checks to see whether the input has been seen before. If it has not, 
# use the function to calculate the  result and save the calculation in a dictionary, where the key is the input and the value is the result. 
# If it has been seen already, look up the result in the dictionary. For the double function given as an example, 
# you should be able to build the relevant dictionary from the reading problems at the beginning of this section.


def Division(number): # Method to return the number divided by the three
    return number / 3

def Check():
    
    n = int(input("Enter a number to loop: "))
    j = 0 
    a = {} #Initialize dictionary
    
    while j in range(n): # loop through until condition is False
        number = float(input("Enter a number: "))
        a[number] = Division(number) #Store the result into a dictionary for first time
        for i in a:
            if number in a: # Check if the number is already in the dictionary
                continue
            else: # Else add it to the dictionary
                a[number] = Division(number)
        j += 1
    
    print("\nEntered numbers with calculations\n")
    for key, value in a.items(): # Looping through the dictionary
        print(f'{key}: {value}')

if __name__ == '__main__':
    Check()
