#Isaiah Wolf 1/31/24
#IsaiahProgram1

speed = 0.00
time = 0.00
distance = 0.00

speed = float(input('Enter the speed the vehicle was travelling(mph)'))
time = float(input('Enter  the amount of time that the vehicle travelled(hours)'))

distance = speed * time

print("Distance Travelled: ", format(distance, ',.2f',), " miles")
