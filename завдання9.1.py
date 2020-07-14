import shutil
import os
import re


f1 = open('data/file1.txt', 'r+')  #відкриття та читання 1го файлу
data1=f1.read()                #запис вмісту в змінну а не файл оскільки недоцільно
f1.seek(0)
f1.truncate()                  #очистка вмісту файлу
f1.close()

f2 = open('data/file2.txt', 'r+')  #відкриття та читання 2го файлу
data2=f2.read()
f2.seek(0)
f2.truncate()                  #очистка вмісту файлу
f2.write(data1)                #запис в чистий 2ий файл данних 1го файлу
f2.close()

fm = open('data/file1.txt','w')
fm.write(data2)               #запис в чистий 1ий файл данних 2го файлу
fm.close()


print(data1)
print(data2)
