#check for y or n
ui = input("would you like an apple pie with that? (y/n) ")


while ui!="y" and ui!="n":
    ui=input("I asked yes or no. (y/n) ")

while not(ui in ["y","Y","n","N"]):
    ui=input("I asked yes or no. (y/n) ")


while not(ui in ["y","yes","n","no"]):
    ui=input("I asked yes or no. (y/n) ").lower()



if ui in ["y","yes"]:
    print("Here's an apple pie")
else:
    print("boo")

