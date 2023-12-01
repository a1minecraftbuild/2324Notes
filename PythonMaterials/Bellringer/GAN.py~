import random

answer = random.randint(1,10)

userInput = int(input("Guess a number between 1 - 10: "))


'''
#My code
while(userInput!=answer):
        if userInput>answer:
            print("Too High")
            userInput = int(input("Try again: "))
        elif (userInput<answer):
            print("Too Low")
            userInput = int(input("Try again: "))
print("Hooray!")
print(answer)
'''
'''
#Banders code
while(userInput!=answer):
    if userInput<answer:
        userInput=int(input("Too low: "))
    elif userInput>answer:
        userInput=int(input("Too high: "))
    else:
        userInput=int(input("Only numbers between 1-10: "))
print("Correct")
'''
#Randy guessing
while(userInput!=answer):
    if userInput<answer:
        print(f"Too high: {answer}")
        answer=random.randint(1,10)
    elif userInput>answer:
        print(f"Too low: {answer}")
        answer=random.randint(1,10)
    else:
        userInput=int(input("Only numbers between 1-10: "))
print(answer)
print("Correct")
