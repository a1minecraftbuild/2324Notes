#read from a text file
#csv file type is a comma seperated version
#each column is seperated or dilhilated by a ,
#print the data on the screen
FILENAME = "2023response.csv"   #ALL CAPS means Constant variable

#with open the file and read the file as variable file:
with open(FILENAME,"r") as file:
        origData=file.readlines()
file.close()
#print(origData)  pukes everything to the terinal

cs=[]


#for row in origData:
for i in range(1,len(origData)):
        #remove the new line in each row
        newRow=origData[i].rstrip() #rstrip() removes all blank spaces to the right
        print(newRow)
        data=newRow.split(".")
        if data[origData[0].split(",")[-1]=="Computer Science Software Development":
                cs.append(newRow)
header=origData[0].rstrip()

#find the amount of scans or length of the file


#save the data to the correct file


