#  Yingjian Yu 65309949 and Chris Gala 94368761.  ICS 31 Lab sec 11.  Lab asst 9.
#Part C
from random import *
NUMBER_OF_STUDENTS = 200
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 4  # 3 choices is A/B/C, 4 choices is A/B/C/D, 5 is A/B/C/D/E

#Part c1
print ('Part c1')
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def generate_answers () -> str:
    n = NUMBER_OF_CHOICES
    ansChoice = ALPHABET[:n]
    answer = ''
    for i in range(NUMBER_OF_QUESTIONS):
        answer += choice(ansChoice)
    return answer
ANSWERS = generate_answers ()
print (ANSWERS)

#Part c2
print ('\nPart c2')
from collections import namedtuple
Student = namedtuple('Student', 'name answers')

def random_students () -> [Student]:
    studentList = []
    for i in range(NUMBER_OF_STUDENTS):
        studentList.append(Student(randrange(99999999), generate_answers ()))
    return studentList
print (random_students ())

#Part c3
print ('\nPart c3')
Student2 = namedtuple('Student2', 'name answers scores total')
def random_students2 () -> [Student]:
    studentList = []
    for i in range(NUMBER_OF_STUDENTS):
        answerStr = generate_answers ()
        scoreList = []
        for i in range(len(answerStr)):
            scoreList.append(int(answerStr[i] == ANSWERS[i]))
        studentList.append(Student2(randrange(99999999), answerStr, scoreList, sum(scoreList)))
    return studentList
print (random_students2())
print()

def total_score (s: Student2)-> int:
    return s.total
studentList = random_students2()
studentList.sort(key =total_score, reverse = True)
for i in range(10):
    print (studentList[i])

sums = 0
for i in studentList:
    sums += i.total
print ('average: ', '{:.1f}'.format(sums/len(studentList)))

#Part c4
print ('\nPart c4')
def generate_weighted_student_answer (s: str) -> str:
    n = NUMBER_OF_CHOICES
    ansChoice = ALPHABET[:n]
    for i in range(randrange(n*2)):
        ansChoice += s
    return choice(ansChoice)
print (generate_weighted_student_answer('C'))

def random_students3 () -> [Student]:
    studentList = []
    for i in range(NUMBER_OF_STUDENTS):
        answerStr = ''
        for i in range(NUMBER_OF_QUESTIONS):
            answerStr += generate_weighted_student_answer(ANSWERS[i])
        scoreList = []
        for i in range(len(answerStr)):
            scoreList.append(int(answerStr[i] == ANSWERS[i]))
        studentList.append(Student2(randrange(99999999), answerStr, scoreList, sum(scoreList)))
    return studentList

studentList = random_students3()
studentList.sort(key =total_score, reverse = True)
for i in range(10):
    print (studentList[i])

sums = 0
for i in studentList:
    sums += i.total
print ('average: ','{:.1f}'.format(sums/len(studentList)))
