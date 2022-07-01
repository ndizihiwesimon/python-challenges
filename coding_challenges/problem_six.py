
# *Problem 6*. You are given an un-ordered array consisting of integers without any duplicates.
# You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order

arr = [2,33,92,100]

timez = 0

for i in range(len(arr)) :
    for j in range(len(arr)):
        if arr[i] > arr[j]:
            timez += 1
    
print(timez)