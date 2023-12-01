'''Data Types:
primitive        integers - +/- whole numbers
primitive        float - +/- decimal number
primitive        boolean - true or false - yes or no - 1 or 0 - smallest data
non-primitive        String - sequence of data combined in one object
non-primitive        List - sequnce of data combined in one object
'''

listy = ["hello","w",0,["r","l","d"]]
# [] indicate a list data type or a sequence
print(type(listy))

backpack=["cheetos","water","pillow","gameboy","compass","pencil"]

print(backpack)
print(backpack[0]) #print out backpack index 0
print(backpack[:2])  #when I say index, the [] should come to mind

characterName = "bob"
characterSkins = "lizard"
characterSpeed = 5
characterSpecial = "TaterGrenade"
characterHealth = 100
characterPoints = 0
characterXP = 1

trentCharacterName = "jimmy"
trentCharacterSkins = "Glasses & PotatoHoody"
tCSp = 3
tcSpec="Timber"
tcH=100
tcP=0
tcXP=7

bekah=["bekah","ninja warrior",7,"Flying",100,0,10]
print(bekah)
tcXP=8
bekah[5]+=5     #adding 5 points to your xp
print(bekah)
bekah[1]="TMNT Warrior"
print(bekah)


randomNumbers=[4,7,8,3,2,8.6,1]
print(sum(randomNumbers))
print(min(randomNumbers))
print(max(randomNumbers))
print(len(randomNumbers))   #length of the list
print(sum(randomNumbers)/len(randomNumbers))

#clear a list
backpack=[]
item=input("What's in your backpack" )
backpack.append(item)   #adds and item to the end of the list
backpack.append(input("What's in your backpack" )
print(backpack)
