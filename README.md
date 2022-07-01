# Python-challenges
These are collections of python code challenges

## Instructions
1. Put each solution in individual module with the same name as the problem (example: problem_one.py)
2. Group all your solutions in one python package called 'coding_challenges'
3. Document your solutions using python comments
4. Don't forget to edit this file to add your name. registration number and department.

## Problems / Challenges
*Problem 1*: Given a list of integers, use a for-loop to find its maximum element; then do the same to find its minimum element.

*Problem 2*. Write a program which checks if a string is palindromic.

*Problem 3*: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

*Problem 4*. Given a list of integers, how many of its elements are multiples of 3? For example, given the list [5, 6, 9, 10, 15, 17, 18, 21], five of its elements are multiples of 3.

*Problem 5*. Given a list of integers, can you find the runner-up? For example, given [2, 3, 3, 6, 4, 5], the maximum is 6 and the runner-up is 5.

*Problem 6*. You are given an un-ordered array consisting of integers without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order

*Problem 7*. Write a function which randomly shuffles a list.

*Problem 8*. Given a list L = [c1 , ..., cn ] of n distinct characters, write a program which generates a random string s such that every character of s is an element of L and such that character ci occurs i times in s.

*Problem 9*:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

*Problem 10*. Write a function that takes two numbers and returns whether the second is a factor of the first.

*Problem 11*. Given a string and a character, write a function that returns how many times the character appears in the string.

*Problem 12*. Write a function that takes two lists and returns the values that are not in the second list, stored in a new list.

*Problem 13*. Write a function that takes 2 lists, and return their intersection.

*Problem 14*. Count the word frequencies in this sentence and store it in a dictionary.
``sonnet1 = [’from’, ’fairest’, ’creatures’, ’we’, ’desire’, ’
increase’,’that’, ’thereby’, ’beauty’,’rose’, ’might’,’
never’, ’die’,’but’,’as’, ’the’, ’riper’, ’should’, ’by’,
’time’, ’decease’,’his’, ’tender’, ’heir’, ’might’, ’
bear’, ’his’, ’memory’,’but’,’thou’, ’contracted’, ’to’,
’thine’, ’own’, ’bright’,’eyes’,’feed’,’thy’,’light’, ’
flame’, ’with’,’self-substantial’,’fuel’,’making’,’a’,’
famine’,’where’, ’abundance’,’lies’,’thyself’,’thy’,’foe’
, ’to’, ’thy’, ’sweet’, ’self’, ’too’, ’cruel’]``

*Problem 15*:
Write a dictionary which takes strings as their keys from user input (using the “input” function), and makes the value the number of times the user has inputted that thing. So, if the user inputs ‘a’, then ‘b‘, and then ’a’, the dictionary should be {’a’: 2, ’b
’: 1}.

*Problem 16*:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods

*Problem 17*. Define a Person class, which takes their name as an argument when it initializes. The person should have a method, greet, which introduces to the user.

*Problem 18*. Write a function of your choosing which takes and returns a number (such as def double(x): return x*2). Write another function which checks to see whether the input has been seen before. If it has not, use the function to calculate the  result and save the calculation in a dictionary, where the key is the input and the value is the result. If it has been seen already, look up the result in the dictionary. For the double function given as an example, you should be able to build the relevant dictionary from the reading problems at the beginning of this section.

*Problem 19*. Implement an ATM, which keeps track of the total amount of money it has. The user should be able to interact with the ATM, and it provide options until they would like to exit. Implement some method, Interact, which allows the user to interact with the ATM.
It should have some methods that the user can select via this interface, which you can implement as you think makes most sense:
1. Withdraw
2. Deposit
3. Current balance
4. Exit

*Problem 20*: Each year the School of Computing Science needs to process exam marks for the students in the department. The highest achieving student gets a price and meets the Head of School. The people who fail a course receive a letter with information about what courses they’ve failed. The School needs to report how the class did on average. To progress to Honours students need to pass all courses and get an average of 70. How many satisfy the requirement? Finally,
each year the Head of School gives a raise to the lecturer of the best performing course. It’s also of interest to know which subject has worst performance. The staff are too busy, so they’ve asked you to write a program that can help them get that information. They’ve helpfully processed it for you, so that all you need is stored in lists.
``marks = [[56,89,70,92,67,100],[60,70,100,45,70,76],
[60,95,90,85,93,45],[55,80,56,45,51,76],[78,100,65,77,91,87],
[45,78,65,50,45,87],[32,50,45,67,40,80]]
students = ["Pelin","Dominique","Valentin","Christine","John Paul","
Patrick","Kellen"]
subjects = ["Algorighms and Data Structures","Java","Web App
Development","Databases", "Human Computer Interaction","
Information Retrieval"]``
