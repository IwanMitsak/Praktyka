import random

def smallestInCol(mat, n, m):
    global dob                      
    dob=1
    for i in range(m):  
        minm = mat[0][i] 
        for j in range(1, n, 1):    
            if (abs(mat[j][i]) < abs(minm)): 
                minm = mat[j][i]    
        print(minm, end = " ")
        dob=dob*minm
    print('\n','Добуток найменших в колонці=',dob)

if __name__ == '__main__': 
    print('Введіть кількість рядків')
    nstr=input()
    nl=int(nstr)
    print('Введіть кількість стовпців')
    mstr=input()
    ml=int(mstr)
    count=0
    full=[]
    
    print('Початкова матриця')
    for _ in range(0,nl):
        list=[]
        while len(list) > 0 : list.pop()
        for i in range(count,count+ml):
            r=random.randint(-10,10)
            list.append(r)                 
            count+=1
        full.append(list)    
        print(*list)
    
    print(' Найменші(по модулю) в стовпцях')
    smallestInCol(full,nl,ml)              
    print('Нова матриця')
    
    print([[j*dob for j in i] for i in full])

