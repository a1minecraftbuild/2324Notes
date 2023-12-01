#from the file import the Class
from Conversions import DistanceConversions
from Conversions import TempConversions
userInterface = '''
            1 - meters to lightyears
            2 - inches to feet
            3 - miles to kilograms
            4 - m/s to f/s
            5 - lb to kg
            6 - K to F
            7 - F to K
            q - quit the program
'''
ui = input(userInterface)
while(ui!="q"):
    if ui=="1":
        meters=int(input("meters: "))
        print(DistanceConversions.metersToLightyears(meters))
    elif ui=="2":
        inches=int(input("inches: "))
        print(DistanceConversions.inToFt(inches))
    elif ui=="3":
        print("Whatever")
    elif ui=="4":
        print("Whatever")
    elif ui=="5":
        print("Whatever")
    elif ui=="6":
        kelvin=int(input("kelvin: "))
        print(TempConversions.kelvinToF(kelvin))
    elif ui=="7":
        fahren=int(input("fahrenheit: "))
        print(TempConversions.fToKelvin(fahren))
    else:
        print("huh?")
    ui = input(userInterface)
