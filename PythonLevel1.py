##
"""1.	Accept a char input from the user and display it on the console."""

x= input("Enter a Character \n")
print ("Your Character is  : ",x[0])


###
"""2.	Accept two inputs from the user and output its sum.”””
Variable	Data Type
Number 1	Integer
Number 2	Float
Sum	Float"""

x= input("Enter a Integer \t:")
x = int(x)
y=input("Enter a Float Number\t:")
y=float(y)
z=x + y
print ('Sum is = ',z)
                        # OR
x=int(input("Enter 1st Value :"))
y=float(input("Enter 2nd Value :"))
print('Sum is : ',(x+y))


##
"""3.	Write a program to find the simple interest.
a.	Program should accept 3 inputs from the user and calculate simple interest for the given inputs. Formula: SI=(P*R*n)/100)
Variable	Data Type
Principal amount (P)	Integer
Interest rate (R)	Float
Number of years (n)	Float
Simple Interest (SI)	Float"""

P = int(input("Principal amount  :"))
R=float(input("Interest rate  :"))
n=float(input("Number of years  :"))

SI=((P*R*n)/100)
print("Simple Interest  = ",SI)


###
"""4.	Write a program to check whether a student has passed or failed in a subject after he or she enters their mark (pass mark for a subject is 50 out of 100).
a.	Program should accept an input from the user and output a message as “Passed” or “Failed”
Variable 	Data type
mark	float"""

R=float(input("Enter Your Mark  :"))
if R>50:
    print("Passed ")
else:
    print("Failed ")


##
"""5.	 Write a program to show the grade obtained by a student after he/she enters their total mark percentage.
a.	Program should accept an input from the user and display their grade as follows
Mark	Grade
> 90	A
80-89	B
70-79	C
60-69	D
50-59	E
< 50	Failed

Variable 	Data type
Total mark	float"""

StudentMark=float(input("Enter Your Mark  :"))

print("Your Grade is \t: ")
if StudentMark>=90:
    print("A ")
elif StudentMark>80 and StudentMark<90:
    print("B ")
elif StudentMark>70 and StudentMark<80:
    print("C ")
elif StudentMark>60 and StudentMark<70:
    print("D ")
elif StudentMark>50 and StudentMark<60:
    print("E ")
else:
    print("Failed ")


##
"""6.	Using the ‘switch case’ write a program to accept an input number from the user and output the day as follows. 
Input	Output
1	Sunday
2	Monday
3	Tuesday
4	Wednesday
5	Thursday
6	Friday
7	Saturday
Any other input	Invalid Entry"""

Day=int(input("Please Enter the Number"))

match Day:
    case 1: 
        print("Sunday") 

    case 2:
        print("Monday")
    
    case 3:
        print("Tuesday")

    case 4: 
        print("Wednesday")

    case 5:
        print("Thursday")

    case 6: 
        print("Friday")
        
    case 7: 
        print("Saturday")

    case _:
        print("Invalid Entry")


##
"""7.	Write a program to print the multiplication table of given numbers. Using for and while
a.	Accept an input from the user and display its multiplication table
Eg: 
Output: Enter a number
Input: 5
Output: 
1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25
6 x 5 = 30
7 x 5 = 35
8 x 5 = 40
9 x 5 = 45
10 x 5 = 50"""

userInput=int(input("Please Enter a Number"))

i=0
while i<10:
    i+=1
    print(i ,"x" ,userInput ,"=",userInput*i )
            #OR
userInput=int(input("Please Enter a Number"))

for i in range(1 ,11):
    print(i ,"x" ,userInput ,"=",userInput*i )


##
"""8.	Write a program to print the following pattern (hint: use nested loop)
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5"""

n = 5      
for i in range(0, n):
        num=1  
        for j in range(0, i + 1):        
            print(num, end=" ")
            num+=1      
        print()  
  

##
"""9.	Write a program to create a copy of array and add an element to copied array . show both arrays.
a.	Program should accept an array from the user, swap the values of two arrays and display it on the console
Eg: Output: Enter the size of Array 1
Input: 5
Output: Enter the values of Array 1
Array 1: 10, 20, 30, 40, 50
Array 2 : Copy of Array 1
Array 2 : 10, 20, 30, 40, 50 + add a element
Output :   Array 1 [10, 20, 30, 40, 50 ]
Output :  Array 2 [10, 20, 30, 40, 50, 60, 70  ]"""

size=int (input("Enter your array size  :"))
array1=[ ]

for i in range(size):
    temp=input("Enter your array element  :")
    array1.append(temp)
    
print(array1)

array2=array1.copy()
array2.extend([3, 5])
print(array2)
            #Or
array1=[ ]
temp=input("Enter your array element  :")
array1.append(temp) 
print(array1)

array2=array1.copy()
array2.extend([3, 5])
print(array2)


##
"""10.	 Write a program to sort an array in descending order without sort() and sorted() Program should accept and array, sort the array values in descending order and display it
●	Selection
●	Insertion
●	bubble

      Eg: Output: Enter the size of an array
Input: 5
Output: Enter the values of array
Input: 20, 10, 50, 30, 40
Output: Sorted array:
50, 40, 30, 20, 10"""

size= int(input("enter Size of the Array"))
Array=[]

for i in range(size):
    Arraytemp=input("Enter array elements")
    Array.append(Arraytemp)

for i in range(1,size):
    for j in range(0,size-1):
        if Array[i]> Array[j]:
            Array[i],Array[j]=Array[j],Array[i]
print(Array)


##
"""11.	Write a program to identify whether a string is a palindrome or not without using reverse(), slicing
a.	A string is a palindrome if it reads the same backward or forward eg: MALAYALAM
Program should accept a string and display whether the string is a palindrome or not
Eg: Output: Enter a string
Input: MALAYALAM
Output: Entered string is a palindrome
Eg 2: Output: Enter a string
Input: HELLO
Output: Entered string is not a palindrome"""

userInput=input("Enter the word to ba checked :")
userInput=userInput.upper()
reversedInput=userInput[::-1]

if userInput==reversedInput:
    print("It is palindrome")
else:
    print("It is not palindrome")


##
"""12.	Write a program to add to two dimensional arrays, understand the memory management of list 
a.	Program should accept two 2D arrays and display its sum
Eg: Output: Enter the size of arrays
Input: 3
Output: Enter the values of array 1
Input: 
1 2 3
4 5 6
7 8 9
Output: Enter the values of array 2
Input:
10 20 30
40 50 60
70 80 90
Output: Sum of 2 arrays is:
11 22 33
44 55 66
77 88 99"""

row = int(input("Enter the number of rows:"))
column = int(input("Enter the number of columns:"))

print("Enter the values of Array1:")
Array1 = []
 
for i in range(row):    
    a = []
    for j in range(column):  
        a.append(int(input()))
    Array1.append(a)

print('Enter the values of Array2:')
Array2 = []

for i in range(row):
    a = []
    for j in range(column):
        a.append(int(input()))
    Array2.append(a)
    
sum_arr = []
for i in range(row):
    a =[]
    for j in range(column):
        a.append(Array1[i][j]+Array2[i][j])
    sum_arr.append(a)
print('Sum of 2 array is:')
for j in sum_arr:
    print(j)


##
"""13.	Grades are computed using a weighted average. Suppose that the written test counts 70%,  lab exams 20% and assignments 10%.
If Arun has a score of
Written test = 81
Lab exams = 68
Assignments = 92
Arun’s overall grade = (81x70)/100 + (68x20)/100 + (92x10)/100 = 79.5
 Write a program to find the grade of a student during his academic year. 
a.	Program should accept the scores for written test, lab exams and assignments
b.	Output the grade of a student (using weighted average)
Eg:
Enter the marks scored by the students
Writtentest = 55
Labexams = 73
Assignments = 87
Grade of the student is 61.8"""

writtenTestMark=float(input("Enter the Test Mark  :"))
labTestMark=float(input("Enter the Lab Mark  :"))
assignmentMark=float(input("Enter the assignment Mark  :"))

total_Grade_In_Percentage=(writtenTestMark*70+labTestMark*20+assignmentMark*10)/100
print("Total Grade In Percentage  :",total_Grade_In_Percentage)


##
"""14.	Study about functions 
⮚	User defined
●	Types of Arguments
⮚	Lambda"""
      
def userDefine(data):
    print ("9 is Greatest") if data < 9 else print("9 is not greatest")

def userLambda(b):
    return lambda a: b*a

userdata=input("enter an Element")
userdata=int(userdata)

userDefine(userdata)
lambdatest = userLambda(userdata)
print(lambdatest(5))


##
"""15.	  Write a program to accept an array and display it on the console using functions
a.	Program should contain 3 functions including main() function
main()
1.	Declare an array
2.	Call function getArray()
3.	Call function displayArray()
		getArray()
1.	Get values to the array
		displayArray()
1.	Display the array values
b.	Study about global, local, non-local"""

def main():
    global userArray
    userArray=[]
    getArray()
    displayArray()

def getArray():
    userArraytemp=input("Enter the array values one by one in commas")
    userArray.append(userArraytemp)
    
def displayArray():
    print(userArray)

main()


##
"""16.	Write a program to print “HELLO WORLD “using function without using print inside of function. (“HELLO WORLD “must be inside Decorator function) 
Code of the program & screenshot of the output."""

def test_fun(func):
        def inner():
                x = func()
                test =x.upper()
                return test
        return inner

@test_fun
def display():
    return "hello world"

print(display())


##
"""17.	 Write a menu driven program to do the basic mathematical operations such as addition, subtraction, multiplication and division (hint: use if else ladder or switch)
a.	Program should have 4 functions named addition(), subtraction(), multiplication() and division()
b.	Should create a class object and call the appropriate function as user prefers in the main function"""

class calculator():
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

    def addition(self):
       Result= self.value1+self.value2
       print("The Sum is",Result)

    def subtraction(self):
        Result= self.value1-self.value2
        print("The Sum is",Result)

    def multiplication(self):
        Result= self.value1*self.value2
        print("The Sum is",Result)

    def division(self):
        Result= self.value1/self.value2
        print("The Sum is",Result)
            
num1=float(input("Enter 1st number"))
num2=float(input("Enter 2nd number"))

choose=int(input("1 = Addition , 2 = Subtraction  , 3 = Multiplication , 4 = Division  :"))
obj1=calculator(num1,num2)
match choose:
        case 1:
            obj1.addition()
        case 2:
            obj1.subtraction()
        case 3:
            obj1.multiplication()
        case 4:
            obj1.division()


##
"""18.	Write a program to print the following pattern using for loop
7 8 9 10 
4 5 6
2 3
1"""

size=4
y=7
x=7
for i in range(size):
    for j in range(size-i):   
        print(y,end=" ")
        y+=1   
    y=y-x
    x=x-2    
    print()
 

##
"""19.	 Write a program to add the values of two 2D arrays
a.	Program should contain a class, Functions should be inside the class
1.	Call function getArray() using an object
2.	Call function addArray() using an object
3.	Call function displayArray() using an object
		getArray()
1.	Get values to the array
		getArray()
1.	Add array 1 and array 2
		displayArray()
1.	Display the array values

Eg:
Enter the size of array
2
Enter the values of array 1
1	2
3	4
Enter the values of array 2
5	6
7	8
Output:
Sum of array 1 and array 2:
6	8
10	12"""

class array_sum():
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col
        self.array1 = []
        self.array2 = []
        self.result_arr = []

    def getArray(self):
        self.row = int(input("Enter the number of rows: "))
        self.col = int(input("Enter the number of columns: "))
        print("Enter the first array values: ")
       
        for i in range(self.row):
              arr = []
              for j in range(self.col):
                arr.append(int(input()))
                self.array1.append(arr)    
       
        print("Enter the second arrray values:")
       
        for i in range(self.row):
            arr = []
            for j in range(self.col):
                arr.append(int(input()))
            self.array2.append(arr)


    def addArray(self):
        self.result_arr = [[0 for _ in range (self.row)] for _ in range(self.col)]
        for i in range(self.row):
            for j in range(self.col):
                self.result_arr[i][j] = self.array1[i][j] + self.array2[i][j]
  
    def displayArray(self):
        print("Sum of array 1 and 2 :")
        for row in self.result_arr:
            print(row)

result=array_sum()
result.getArray()
result.addArray()
result.displayArray()

##
"""20.	Write a program to include all the functionalities of a calculator using ABSTRACT class 
and abstract method. All the methods (add, sub, mul, div) should be inside of abstract class. 
Abstract method definition should be in another class. """

"""Examples : 
from abc import ABC, abstractmethod
 class Calculator(ABC): 
         def __init__(self, id, name): 
              self.id = id self.name = name
        @abstractmethod 
        def add (self): 
                   pass"""

from abc import ABC,abstractmethod

class Calculator(ABC):
    @abstractmethod
    def add(self, num1, num2):
        pass
    @abstractmethod
    def sub(self, num1, num2):
        pass
    @abstractmethod
    def multi(self, num1, num2):
        pass
    @abstractmethod
    def div(self, num1, num2):
        pass

class Calcfunc(Calculator):
    def add(self, num1, num2):
        result = num1 + num2
        print('Result of addition: ', result)
        return result
    def sub(self, num1, num2):
        result = num1 - num2
        print('Result of substraction:', result)
        return result
    def multi(self, num1, num2):
        result = num1 * num2
        print('Result of multiplication:', result)
        return result
    def div(self, num1, num2):
        result = num1 / num2
        print('Result of division:', result)
        return result

calculator = Calcfunc()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = calculator.add(num1, num2)
result = calculator.sub(num1, num2)
result = calculator.multi(num1, num2)
result = calculator.div(num1, num2)

##
"""21.	Write a program to build a home. The Home class should define all the attributes of each room in a home. From the Home class create two homes. FirstHome and SecondHome. First home should have an extra study room as a method. SecondHome should have the work_area as an extra method. should use the concept of inheritance.
class Home:"""


##
"""22.	Write a program to create Class with name and account number and implement 
get and set, with property decorator and making account number and name private."""

class Bankaccount:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,newname):
        self._name = newname
    @property
    def number(self):
        return self._number
    @number.setter
    def number(self,newnumber):
        self._number = newnumber
display = Bankaccount(name='LionByte',number=43530000010003235)
print('Name :',display.name)
print('Account number:',display.number)

display.name = 'Mr.LionByte'
display.number = 43530000010003235
print('New name:',display.name)
print('New Acc number:',display.number)

##
"""23.	Write a function to calculate the sum of all numbers passed as its arguments. Your function should be called sum_numbers and should define a single variable             argument (i.e. a star argument) that will get the values to sum.

      Test the function with the following values:

Values                Result
1, 2, 3                      6
8, 20, 2                    30
12.5, 3.147, 98.1    113.747
             1.1, 2.2, 5.5           8.8"""

def sum_numbers(*arg):
    return sum(arg)

Answer= sum_numbers(1,2,3)
print("Result is :",Answer)

Answer= sum_numbers(8, 20, 2)
print("Result is :",Answer)

Answer= sum_numbers(12.5, 3.147, 98.1)
print("Result is :",Answer)

Answer= sum_numbers(1.1, 2.2, 5.5 )
print("Result is :",Answer)

##
"""24.	pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": [
        "chicken",
              "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}


observe the dictionary above and write a menu driven python program to create recipes. Once one recipe is done then the quantity of the items in pantry should also be reduced
Eg  :  If you cook beans on toast the beans quantity and bread quantity need to decrease i.e., one from the total quantity each."""

Pantry = {    
    "chicken": 500,
    "lemon": 2,
    "beans": 10,
    "bread": 20,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
    "potato": 9,
}

recipes = {
    "Butter chicken": [
        "chicken", "lemon", "cumin", "paprika", "chilli powder", "yogurt", "oil", "onion", "garlic", "ginger",
        "tomato puree", "almonds", "rice", "coriander", "lime",
    ],
    "Chicken and chips": [
        "chicken", "potato", "salt", "malt vinegar",
    ],
 "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg", "bread", "butter",
    ],
    "Beans on toast": [
        "beans", "bread",
    ],
    "Spam a la tin": [
        "spam", "tin opener", "spoon",
    ],
}

while True:
    your_input = input(
"""
Enter the Recipe You need to make,
Available Items
1. Butter chicken
2. Chicken and chips
3. Pizza
4. Egg sandwich
5. Beans on toast
6. Spam a la tin
7.  Quit
Choose here:
"""
)
    if your_input.strip() in recipes:
        for recipe, ingredients in recipes.items():
            if your_input.strip() == recipe:
                for ingredient in ingredients:
                    if ingredient in Pantry:
                        Pantry[ingredient] -= 1
                        print(f"Available Count of {ingredient}:", Pantry[ingredient])

    elif your_input == "7":
        break


##
"""25.	create a custom exception class and raise this exception when the user presses one in the menu and handles this exception."""

class Error_rr(Exception):
 pass
number = 1

try:
    num = int(input("Enter a number: "))
    if num==number:
        raise Error_rr
    else:
        print("number:",num)
       
except Error_rr:
    print("Exception occurred: number error")

##
"""26.	Write a list comprehension that returns the list ["1*2=1", "22=4", "32=9", ...., "25*2=625"]"""

list1=[f"{i} x 2 = {i**2}" for i in range(1,26) ]
print(list1)

##
"""27.	Using dict comprehension and a conditional argument create a dictionary from the current dictionary where only 
the key:value pairs with value above 2000 will be taken to the new dictionary."""

dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={}
dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={}
dict2={key:value for key,value in dict1.items() if value>2000 }
print(dict2)
