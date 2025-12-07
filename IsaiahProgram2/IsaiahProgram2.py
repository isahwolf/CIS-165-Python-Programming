#Isaiah Wolf 2/14/24
#IsaiahProgram2.py

areaA = 0.0
areaB = 0.0
radiusA = 0.0
radiusB = 0.0
pie = 3.14159

radiusA = float(input('Enter the Radius for Circle A: '))
radiusB = float(input('Enter the Radius for Circle B: '))

areaA = radiusA * radiusA * pie
areaB = radiusB * radiusB * pie

print('Area for Circle A =', format(areaA, ',.2f'))
print('Area for Circle B =', format(areaB, ',.2f'))
    
if areaA > areaB:
    print('Area for Circle A is greater than Area for Circle B')
elif areaA < areaB:
    print('Area for Circle B is greater than Area for Circle A')
else:
    print('Area for Circle A is equal to the Area for Circle B')
