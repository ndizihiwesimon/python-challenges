# *Problem 10*. Write a function that takes two numbers and returns whether the second is a factor of the first.

def isFactorOf(a, b):
    if a % b == 0: # Condition to check if the second is a factor of the first
        return print(a, "Is a factor of", b)
    else:
        return print(a, "Is not a factor of", b)

isFactorOf(2, 2)
        