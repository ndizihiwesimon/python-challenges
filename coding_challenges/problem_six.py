
# *Problem 6*. You are given an un-ordered array consisting of integers without any duplicates.
# You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order

from os import times


arr = [2,33,92,100]

times = 0

for i in range(len(arr)) :
    for j in range(len(arr)):
        if arr[i] > arr[j]:
            times += 1
    
print(times)