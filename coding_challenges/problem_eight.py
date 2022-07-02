# *Problem 8*. Given a list L = [c1 , ..., cn ] of n distinct characters, 
# write a program which generates a random string s such that every character of s is an element of L and such that character ci occurs i times in s.

import random

def randomString(n):
    # Given a List of of distinct characters
    L = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z']
    
    # Variable to store generated random string
    s = ""

    # Generate a random string
    for i in range(n):
        s = s + L[random.randint(0,len(L)-1)]
    
    return s

# Displaying random string
print(randomString(5))

