import math

def area():
    length = float(input('Enter length: '))
    width = float(input('Enter width: '))
    area = length * width
    print(area)
area()

def circumference():
    r = float(input('Enter radius of circle: '))
    circumference = 2 * math.pi * r
    print(circumference)
circumference()