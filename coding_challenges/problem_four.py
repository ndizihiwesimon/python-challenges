# List of integers
TheList = [5, 6, 9, 24, 10, 15, 17, 18, 21]

# Variable that holds the number of numbers divisible by 3
yes = 0

# Looping through the list of integers
for i in range(0, len(TheList)):
    # Checking if the number is divisible by 3
    if TheList[i] % 3 == 0:
        yes += 1
        
# Displaying result on terminal
print(yes, "of elements are multiples of 3")