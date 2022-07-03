# *Problem 20*: Each year the School of Computing Science needs to process exam marks for the students in the department. 
# The highest achieving student gets a price and meets the Head of School. The people who fail a course receive a letter with information about what courses they’ve failed. 
# The School needs to report how the class did on average. 
# To progress to Honours students need to pass all courses and get an average of 70. 
# How many satisfy the requirement? Finally,
# each year the Head of School gives a raise to the lecturer of the best performing course. 
# It’s also of interest to know which subject has worst performance. 
# The staff are too busy, so they’ve asked you to write a program that can help them get that information. 
# They’ve helpfully processed it for you, so that all you need is stored in lists.
# 
# ``marks = [[56,89,70,92,67,100],[60,70,100,45,70,76],
# [60,95,90,85,93,45],[55,80,56,45,51,76],[78,100,65,77,91,87],
# [45,78,65,50,45,87],[32,50,45,67,40,80]]
# 
# students = ["Pelin","Dominique","Valentin","Christine","John Paul","
# Patrick","Kellen"]
# 
# subjects = ["Algorithms and Data Structures","Java","Web App Development","Databases", "Human Computer Interaction", "Information Retrieval"]``


from audioop import avg


class Department:
    def __init__(self):
        self.Students = []
        self.Subjects = []
        self.Marks = []
    
    def subjects(self):
        n = int(input("Enter number of Subjects: "))
        for i in range(n):
            self.Subjects.append(input("Enter Subject name: "))

    def students(self):
        n = int(input("Enter number of Students: "))
        for i in range(n):
            self.Students.append(input("Enter Student name: "))

    def marks(self):
        stud = len(self.Students)
        obj = len(self.Subjects)
        studMarks = []
        studSum = 0.00
        studAvg = 0.00
        avgDict = {}
        for i in range(stud):
            print("Record %s marks: \n" % self.Students[i])
            for j in range(obj):
                mrk = float(input("Enter %s marks: " % self.Subjects[j]))
                studMarks.append(mrk)
                studSum += mrk
            self.Marks.append(studMarks)
            studAvg = studSum / obj
            avgDict[self.Students[i]] = studAvg
    


    def get_marks(self):
        stud = len(self.Students)
        obj = len(self.Subjects)
        for i in range(stud):
            print("Below is %s marks: \n" % self.Students[i])
            for j in range(obj):
                print("%s : %d" % (self.Subjects[j], self.Marks[i][j]))



if __name__ == "__main__":
    department = Department() #Created object for department

    department.subjects()
    department.students()
    department.marks()
    department.get_marks()
