import os
fname='data/student.txt'    #шлях до файлу

print('''
Введіть команду :
1.Запис у файл
2.Прочитати файл
3.Дозапис у файл
4.Обрати файл
5.Пошук даних у файлі
6.Посортувати за середнім балом
7.Вихід''')

while True:
    print("\nВведіть команду")
    command = input()
    
    if command == '1':
        text=input("Введіть рядок, який бажаєте записати у файл: ")
        f = open(fname, "w")    
        f.write(text)         #відкриття файлу та запис в нього рядка
        f.close()             #формат рядка : Ім'я студента - Бал
        
    elif command == '2':
        file = open(fname, 'r')
        print('File ' + fname + ':')
        for line in file:
            print(line, end='')
        file.close()
        
    elif command == '3':
        text=input("Введіть рядок, який бажаєте дозаписати у файл: ")
        f = open(fname, "a")
        f.write('\n')
        f.write(text)        #відкриття файлу та запис в нього рядка
        f.close()
        
    elif command == '4':
        flag=False
        folder=input("Введіть шлях до каталогу, у якому бажаєте шукати файл: ")
        for d, dirs, files in os.walk(folder):
            for f in files:
                if f==fname: #відкриття вікна вибору файлу 
                    flag=True
                    path = os.path.join(d,f)
        if flag == True:
            print("Файл існує "+path)
        else:
            print("Такого файлу не існує "+folder)
            
    elif command == '5':
        word=input("Введіть пошуковий запит: ")
        file = open(fname, 'r')
        for line in file:    #пошук слова у рядку у файлі
            if word in line:
                print(line, end='')
                
    elif command == '6':
        f = open(fname,'r+')
        d=f.readlines()
        d.sort(key=lambda l: float(l.split(" - ")[1])) # сортування рядків за середнім балом
        f.seek(0)
        f.write("".join(d))
        print("Відсортовано за балом.")
        f.close()
        
    elif command == '7':
        break                                          #вихід з циклу та програми
    else:
        print('ERROR')
