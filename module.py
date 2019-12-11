def printName(name):
    print("The name printed from this file is:", name)
    
def sqrfoot():
    length = int(input("What's the length of the house?"))
    width = int(input("And its width?"))
    return length * width
                 
def circumf():
    radius = int(input("What's the radius of the circle?"))
    from math import pi
    return pi * radius ** 2
