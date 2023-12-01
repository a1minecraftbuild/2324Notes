#String - non-primitive data type
#   sequence of things put together
#sequence - combination or collection of info
#   type of data structure
#   list, tuple, dictionary, Array, ArrayList

name = "Billy"
password = "123456"

#Strings can be identified by " or '
#   BUT for every quote " you need an end "

output = f"Welcome, {name}!"
#{} are injection points for variables
stuff = f"Here is 2+2={2+2}"

'''
    In other languages:
            "String Value" + mathvalue -> would error
        f"" with the {} converts all the data for you
'''

f'''
    Another way of doing an f string
        Here are some variables.
            {output}
            {stuff}
'''

# Escape Characters - special characters that do stuff
#\n -> enter button -> adds a new line
#\t -> tab button - adds a tab
#\s -> space button - adds a space
#\" -> quote button - adds a quote to you output

print("2"*3)    #This will multiply the amount of strings
print("="*50)
print("\n"*5)  #simulates clearing the screen

username = "lordBander"
email = username+"@evsck12.com"
print(email)

domain = email[10:]     #Grabbing a portion or substring of email
print(domain)
#stringObject.method() or object.method()
#button1.click()
domain = email[email.index("@"):]   #index(chr) grab first occurance of chr
print(domain[0:domain.index(".")])
'''
        stringObject[:#] this grabs from beginning to a value
        stringObject[#:] this grabs from value to end
        stringObject[#:3] this grabs from value and 3 more chr
'''

first="bob"
last="saget"
scifiFirst = first[0:2]+last[2:]
print(scifiFirst)
