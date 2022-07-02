# *Problem 11*. Given a string and a character, write a function that returns how many times the character appears in the string.

def HowManyTimes(string, character):
    count = 0
    for i in range(len(string)):
        if (string[i] == character) or (string[i] == str(character).capitalize()):
            count += 1
    return count

def main():
    string = input("Please enter a string: ")
    character = input("Please enter a character: ")
    count = HowManyTimes(string, character)
    print(count)

if __name__ == '__main__':
    main()
