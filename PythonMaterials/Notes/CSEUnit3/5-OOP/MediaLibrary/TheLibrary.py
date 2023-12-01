#imports
from Song import Song

#global var
menu=""
library=[]
#create a song
#myfav = Song("Cradles - Sub Urban")

#print(myfav)
#print(object's character)
#print(myfav.title)

#define functions

#main loop
while menu != "q":
    menu=input('''
        a - add song
        e - edit song
        d - delete song
        v - view library
        q - quit the program
    ''')
    if menu=="a":
        name = input("Name of your song ")
        artist=input("Name of artist ")
        library.append(Song(name,artist))
        print("add a song")
    elif menu=="e":
        print("edit a song")
    elif menu=="d":
        print("delete a song")
    elif menu=="v":
        print(library)
        for eachItem in library:
            print(eachItem)#eachItem.title + eachItem.artist)
    elif menu!="q":
        print("error: that is not a valid input")
print("program quit, data error")
