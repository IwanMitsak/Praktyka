print('Введіть перше слово')
word1 = input()
print('Введіть друге слово:')
word2 = input()
x=list(word1)
y=list(word2)
final=[]
listsum=x+y                     
listsum.sort()

#print(listsum)
_size = len(listsum) 
repeated = [] 
for i in range(_size): 
    k = i + 1
    for j in range(k, _size):
        if listsum[i] == listsum[j] and listsum[i] not in repeated: 
            repeated.append(listsum[i]) 

final=set(listsum)-set(repeated)

print('Літери які не повторяються :',final)
