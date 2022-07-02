# Write a function which randomly shuffles a list.

import random

# list of 0 to 5 
l = list(range(5))

# before shuffle
print("Before shuffling...",l)


random.shuffle(l)
# After shuffle
print("After shuffling...",l)