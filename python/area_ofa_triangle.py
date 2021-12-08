import math
a = float(input('Enter the first side : '))
b = float(input('Enter the second side : '))
c = float(input('Enter the third side : '))
s = (a+b+c)/2
area_triangle = math.sqrt(s*(s-a)*(s-b)*(s-c))
print('Area of triangle : ',area_triangle)