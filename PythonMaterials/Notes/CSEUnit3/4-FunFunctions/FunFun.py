#Functions make abstract ideas of complex algorithms.  
#adding two numbers
#define theFunctionAddTwoNumber(that needs a and b):
def addTwoNumber(a,b):
    print(a+b)

#define a function that subtracts two numbers
def subtractTwoNumbers(a,b):
    print(a-b)

#define a function that says hi
def sayHi():
    print("hi")

print("calls the function")
sayHi()
addTwoNumber(5,9)
subtractTwoNumbers(3,2)

#the distance function
import math
def distanceFormula(x1,x2,y1,y2):
    print(math.sqrt((x2-x10)**2+(y2-y1)**2))

distanceFormula(2,0,5,4)
#for i in range(10):
#    distanceFormula(i,0,5,4)

#quadratic function
def quadraticFormula(a,b,c):
    pos=(-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
    neg=(-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
    print(pos,neg)

#quadraticFormula(1,2,3)
#quadraticFormula(3,2,3)
#quadraticFormula(1,2,3)
#quadraticFormula(1,2,1)

#define a function that will keep asking the user for "guess what" until they type in "dude what?"
def guessWhat():
    answer = input("guess what")
    while answer != "dude what?":
        answer = input("guess what")


guessWhat()
print("chicken butt")

#define a function that keeps asking the user for a question until the answer is in a list of correct answer

#what is your favorite of ice cream
#correctAnswer = "cookies n cream" "cookie dough" "strawberry" "peach cobbler" "grandpas homemade chocolate icecream"

def userInput(question,correctAnswer):
    ui=input(question)
    while(not (ui in correctAnswer)):
        ui=input(question)
    return ui


ui=userInput("Fav ic cream?",["yes","everything","not vanilla","peach cobbler"])
print(ui)



