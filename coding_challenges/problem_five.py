
# List of integers
TheList = [5, 6, 9, 24, 10, 15, 17, 18, 21, 22, 24]

# Sorting array in descending order
arr = sorted(TheList, reverse=True)

# Looping through the list of integers
for i in range(len(TheList)):
    # Check if two numbers are equal and skip
    if arr[i] == arr[0]:
        continue
    # If the number is not equal to the current value, print it out
    else:
        print(arr[i])
        break

