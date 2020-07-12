import math
import itertools

def f(x,k):
    return pow(-1,k-1)*pow(x,k)
e=0.001
a=-0.9
b=1

k=0
i=0
print('X   ','f(x)','f(x)набл','eps  ','iteration')
for x in itertools.count(start=a,step=0.2):
    if x>b:
        print('break')
        break
    tmp=f(x,k)
    result=tmp
    if 1+x == 0:
            ex='NULL'
    else:
            ex = 1/(1+x)
    while(abs(tmp)>=e):
            k+=1
            i+=1
            tmp=f(x,k)
            result+=x
    print(x,ex,result,e,k)
print('Загальна к-сть ітерацій:',k)
