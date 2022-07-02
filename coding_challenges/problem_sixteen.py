# *Problem 16*:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods

class Problem16():
    def getString():
        hello = input('Enter a string: ')
        return hello
    
    def printString():
        print("Entered string: ", Problem16.getString())

if __name__ == '__main__':
    Problem16.printString()
