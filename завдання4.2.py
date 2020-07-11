print('Введіть текст (латинського алфавіту)')
text=input().lower()

gol = set("aeiouy")                 
prug = set("bcdfghjklmnpqrstvwxz")  

count_gol = 0
count_prug = 0
for c in text:
    if c in gol:
        count_gol += 1
    elif c in prug:
        count_prug += 1
if count_gol == count_prug:
    print('draw')
print('Приголосних більше' if count_prug > count_gol else 'Голосних більше')
