import math

def square(side):
    
    area = side ** 2
    return math.ceil(area)

side_length = 3.6
area_result = square(side_length)

print(f"Площадь квадрата со стороной {side_length}: {area_result}")