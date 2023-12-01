#define the class
class Song:
        #define the constructor
        def __init__(self,t,a):
                #object.attribute = variablePassedIn
                self.title=t
                self.artist=a
        #toString method -> whenver you print the obj, this is what will print        
        def __str__(self):
                #in other words you overwritting the Song, Song at x89237904874632
                out=""
                out+=self.title+"\n\t"
                out+=self.artist+"\n\t"
                return out
        #getters and setters

        #any methods that the objects can do

        #static methods

