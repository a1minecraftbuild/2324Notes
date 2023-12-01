orderInformation=""
total = 0
sandwich = input("Would you like a sandwich? (y/n) ")
if sandwich == "y":
    sandwich = input("Which sandwich would you like?  Chicken (c) for $5.25, beef (b) $6.25, tofu (t) $5.75 ")
    #conditional statement that adds to the total cost.
    if sandwich == "c":
        total+=5.25 #add 5.25 to total
        sandwich="chicken sandwich"
    elif sandwich == "b":
        total+=6.25
        sandwich="beef sandwich"
    elif sandwich == "t":
        total+=5.75
        sandwich="tofu sandwich"
    else:
        print("Huh?")
orderInformation+=f"Sandwich:\t{sandwich}\n"

print(sandwich)

drink = input("Would you like a drink? (y/n) ")
if drink == "y":
    drink = input("What size, small (s), medium (m), or large (l)? ")
    if drink == "s":
        total+=1
        drink="small"
    elif drink == "m":
        total+=1.75
        drink="medium"
    elif drink == "l":
        total+=2.25
        drink=input("Would you like to upgrade it to a child sized cup for 38 cents? (y/n) ")
        if drink == "y":
            drink = "child-sized cup"
            total+=0.38
        else:
            drink = "large"
orderInformation+=f"Drink:\t{drink}\n"

fries = input("Would you like fries? (y/n) ")
if fries == "y":
    fries = input("What size, small (s), medium (m), or large (l)? ")
    if fries == "s":
        total+=1
        fries="small"
        fries=input("Would you like to upgrade it to mega sized fries for 50 cents? (y/n) ")
        if fries == "y":
            fries = "mega-sized fries"
            total+=0.50
        else:
            fries = "small"
    elif fries == "m":
        total+=1.50
        fries="medium"
    elif fries == "l":
        total+=2.00
        fries="large"
orderInformation+=f"Fries:\t{fries}\n"
if sandwich != "n" and drink != "n" and fries != "n":
    total = (total - 1.00)
ketchup = int(input("How many ketchup packets would you like? (Positive Whole Number) "))
total += (ketchup*0.25)
orderInformation+=f"Ketchup Packets:\t{ketchup}\n"
total += (total*.07)
total = (round(total,2))
print(orderInformation)
print(f"${total}")
