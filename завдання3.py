import random
print('Vvedit diapazon:')
n=int(input())
our_arr = random.sample(range(-10, 10), n)   
new_arr=[]
print('Masuv:',our_arr)

pos = next((x for x, val in enumerate(our_arr) if val > 0),None) 
 
new_arr=our_arr[pos:]   
                                                                 
if pos!=None:            
    print('Suma elementiv do ostannogo dodatnogo 4usla: ',sum(new_arr))
else:
    print('Nemae dodatnih 4usel')
