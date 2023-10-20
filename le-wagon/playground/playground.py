# TODO: it's a playground, let's write some code (no unit tests to run here)

# Types and Variables Section 
radius = 5 

from math import pi

perimeter = 2 * radius * pi 

print(perimeter)

area = pi *(radius**2)

print(area)


radius2= 5

print(f"The radius is set to {radius2}")

perimeter2 = 2 * pi * radius2

print(f"Perimeter of the circle is {round(perimeter2,1)}")

area2 = pi * (radius2**2)

print(f"Area of the disk is {round(area2,1)}")

#Function Section

import math 

def circle_math(radius):
    perimeter = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return(round(perimeter, 1), round(area, 1))

values = circle_math(5)
print(f"Radius=5 => Perimeter={values[0]}, Area={values[1]}")

values = circle_math(6)
print(f"Radius=6 => Perimeter={values[0]}, Area={values[1]}")

