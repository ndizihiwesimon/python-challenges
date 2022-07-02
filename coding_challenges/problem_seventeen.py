# *Problem 17*. Define a Person class, which takes their name as an argument when it initializes. 
# The person should have a method, greet, which introduces to the user.

# Person class
class Person:
    def __init__(self, name): # Initialize the class with the name specified
        self.name = name
    
    # Greet person method
    def greet(self):
        return print("Greetings, %s" % self.name)

person = Person(input("Enter your name: "))
person.greet()
