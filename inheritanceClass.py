'''
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has 4 parameters:
A string,firstName .
A string, lastName.
An integer,idNumber .
An integer array (or vector) of test scores,scores .
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
Grading scale
90<=a<=100=>O
80<=a<=90=>E
70<=a<=80=>A
55<=a<=70=>P
40<=a<=55=>D
a<40=>T

Sample Input

Heraldo Memelli 8135627
2
100 80
'''
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName, lastName, idNum , scores):

        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
        self.scores = scores
    
    def printPerson(self):
        print("Name: " + lastName + ", " + firstName)
        print("ID:", idNum)
    
    def calculate(self):
        x = len(scores)
        n = 0
        for i in range(x):
            n+=scores[i]
        
        y = int(n)//int(x)

        if 90<= y <= 100:
            return 'O'
        elif 80<= y < 90:
            return 'E'
        elif 70<= y < 80:
            return 'A'
        elif 55<= y < 70:
            return 'P'
        elif 40<= y < 55:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())