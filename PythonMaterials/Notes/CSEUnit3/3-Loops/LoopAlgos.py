#create a list of 10 random integers
#output the average of the 10 random integers
#integers need to be from 933 and 1866
lo,hi=933,1866  #good practice when same idea
mid = int((hi+lo)/2)
import random
listy=[1]
ave=sum(listy)/len(listy)
while (not(ave>(mid*.95) and ave<(mid*1.05))):
    listy=[]
    for i in range(10):
        number=random.randint(lo,hi)
        listy.append(number)
    ave=sum(listy)/len(listy)
    print(ave)
print(listy)



#the average of the list of numbers we generate are within 5% of the midpoint


ui="!$%()()(\'*&%#))*((\""
left,right=0,0
#for eachItem in sequence
#for eachChr in ui:
for i in range(len(ui)):
    print(i)
    if ui[i]=="(":
        left+=1
    elif ui[i]==")":
        right+=1
    #if left!=right:
print(left,right)
#find the amount of (
#find the amount of )
#if they don't match, point out what index doesn't match
'''
        two types of for loops
            foreach loop
                for eachItem in sequence
            traditional for loop
                for i in range(len(sequence))
'''
