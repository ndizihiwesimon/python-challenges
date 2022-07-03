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


class Department:
    # Initialize the department
    def __init__(self):
        self.Students = []
        self.Subjects = []
        self.Marks = []
        self.TotalMarks = 0
        self.avgDict = {}
        self.StudTotalMarks = {}
        self.StudFeedback = {}
    
    # Method for creating the subjects
    def subjects(self):
        n = int(input("Enter number of Subjects: \n"))
        self.TotalMarks = n * 100
        for i in range(n):
            self.Subjects.append(input("Enter Subject name: "))
   
    #  Method to record students
    def students(self):
        n = int(input("\nEnter number of Students: \n"))
        for i in range(n):
            self.Students.append(input("Enter Student name: "))

    #  Method that calculate and generates marks for students
    def marks(self):
        stud = len(self.Students)
        obj = len(self.Subjects)
        studSum = 0.00
        studAvg = 0.00
        for i in range(stud):
            print("\nRecord %s marks out of 100: \n" % self.Students[i])
            studMarks = []
            for j in range(obj):
                mrk = float(input("Enter %s marks: " % self.Subjects[j]))
                studMarks.append(mrk)
                studSum += mrk
            self.Marks.append(studMarks)
            studAvg = studSum / obj
            if studAvg >= 70:
                self.StudFeedback[self.Students[i]] = "Honours"
            elif studAvg < 70 >= 50:
                self.StudFeedback[self.Students[i]] = "Pass"
            else:
                self.StudFeedback[self.Students[i]] = "Fail"
            self.StudTotalMarks[self.Students[i]] = studSum
            self.avgDict[self.Students[i]] = studAvg
            studSum = 0.00
            studAvg = 0.00
    

    #  Method to display results
    def get_marks(self):
        stud = len(self.Students)
        obj = len(self.Subjects)
        for i in range(stud):
            print("\nBelow is %s marks: \n" % self.Students[i])
            for j in range(obj):
                print("%s : %d" % (self.Subjects[j], self.Marks[i][j]))
            print("\n")
            print("================================")
            print("Total marks: %d out of %d " % (self.StudTotalMarks.get(self.Students[i]), self.TotalMarks))
            print("Average marks: %d out of 100 " % self.avgDict.get(self.Students[i]))
            print("Feedback: %s " % self.StudFeedback.get(self.Students[i]))
            print("\n")

if __name__ == "__main__":
    department = Department() #Created object for department

    department.subjects()
    department.students()
    department.marks()
    department.get_marks()
