# *Problem 18*. Write a function of your choosing which takes and returns a number (such as def double(x): return x*2). 
# Write another function which checks to see whether the input has been seen before. If it has not, 
# use the function to calculate the  result and save the calculation in a dictionary, where the key is the input and the value is the result. 
# If it has been seen already, look up the result in the dictionary. For the double function given as an example, 
# you should be able to build the relevant dictionary from the reading problems at the beginning of this section.


def Remainder(number):
    return number % 2

def Check():
    
    n = int(input("Enter a number to loop: "))
    j = 0
    while j in range(n):
        number = int(input("Enter a number: "))
        a = {}
        for i in range(n):
            if number in a:
                continue
            else:
                a[number] = Remainder(number)

        for key, value in a.items():
            print(f'{key}: {value}')
        j += 1

if __name__ == '__main__':
    Check()
