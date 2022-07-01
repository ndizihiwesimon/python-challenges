
# List of integers
TheList = [5, 6, 9, 24, 10, 15, 17, 18, 21, 22, 24]

arr = sorted(TheList, reverse=True)

for i in range(1, len(TheList)):
    if arr[i] == arr[0]:
        continue
    else:
        print(arr[i])
        break

