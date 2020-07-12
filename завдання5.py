import random

numlist=[]
for i in range(0,25):
    n = random.randint(-5,5)     
    numlist.append(n)
print(numlist)

def findzero(x):                
    for i, j in enumerate(x):
        if j == 0:
            print('Число з цим індексом нуль - ',i)

zeros=findzero(numlist)         
print(zeros)
