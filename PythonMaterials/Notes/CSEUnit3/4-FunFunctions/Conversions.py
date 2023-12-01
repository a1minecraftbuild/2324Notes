#Schlusemeyer
#this file contains all of the math for our conversions
#defined the class converter:
class DistanceConversions:
    #first is capitalized bc it is a Class
    #all the functions for our Unit Converter
    #static method -> a method you can run without an object
    @staticmethod   #@ sign is a decorator
    def inToFt(inches):
        return inches/12

    @staticmethod
    def metersToLightyears(meters):
        return meters/9.46e+15
class TempConversions
    @staticmethod
    def fToKelvin(fahren):
        return (fahren-32)/1.8+273.15

    @staticmethod
    def kelvinToF(kelvin):
        return kelvin*1.8-459.67
