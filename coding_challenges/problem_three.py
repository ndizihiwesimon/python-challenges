
# For loop that go through all numbers
for number in range(2000, 3200):
    # checking whether the number is divisible by 7 and NOT Multiple of 5
    if number % 7 == 0 and number % 5 != 0:
        print(number, end=", ")