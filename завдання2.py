x = int(input('Vvedit 4uslo x: '))
dx = 0.4
import math
while x >= 0 and x <= 2 :
    z = ((x**3)+2*x)/(3*math.cos(math.sqrt(x))+1)
    x += dx
    print (z)
 	 	 
