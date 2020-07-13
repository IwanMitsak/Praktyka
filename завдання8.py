class Product:
    def __init__(self, price, model, year):
        self.price = price
        self.model = model
        self.year = year
    def print(self):
        print(self.__class__.__name__)
        print('Модель:', self.model)
        print('Ціна: ', self.price)
        print('Рік:', self.year)
    def search(arr, key):
        flag=True
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == key:
                    k=i
                    flag = False
                    for m in range(len(arr[i])):
                        print(arr[k][m],end=' ')
                    print()
        print()
        print()
        
class Laptop(Product):
     def __init__(self, price, model, year, diag):
        Product.__init__(self, price, model, year)
        self.diag = diag
     def print(self):
        super().print()
        print('Діагональ екрана: ',self.diag)
        print()

class PC(Product):
    def __init__(self, price, model, year, cdbay):
        Product.__init__(self, price, model, year)
        self.cdbay = cdbay #привід
    def print(self):
        super().print()
        print('Наявність приводу: ',self.cdbay)
        print()
 
class Server(Product):
     def __init__(self, price, model, year, cdbay,stype):
        Product.__init__(self, price, model, year)
        self.cdbay = cdbay #привід
        self.stype = stype #тип сервера
     def print(self):
        super().print()
        print('Наявність приводу: ',self.cdbay)
        print('Тип сервера: ',self.stype)
        print()
    


laptop1=Laptop(20999,'Asus',2017,26)
laptop2=Laptop(35199,'Acer',2020,30)
laptop3=Laptop(17499,'Dell',2015,24)

arrLaptop=[[laptop1.price,laptop1.model,laptop1.year,laptop1.diag],
           [laptop2.price,laptop2.model,laptop2.year,laptop2.diag],
           [laptop3.price,laptop3.model,laptop3.year,laptop3.diag]]

pc1=PC(28199,'Intel',2018,'оптичний')
pc2=PC(50211,'MSI',2020,'оптичний')
pc3=PC(15299,'AMD',2016,'не оптичний')

arrPC=    [[pc1.price,pc1.model,pc1.year,pc1.cdbay],
           [pc2.price,pc2.model,pc2.year,pc2.cdbay],
           [pc3.price,pc3.model,pc3.year,pc3.cdbay]]

server1=Server(12099,'JHIH6',2020,'оптичний','шафовий')
server2=Server(15199,'SFA23',2019,'не оптичний','шафовий')
server3=Server(9790,'AHFI3',2018,'оптичний','підлоговий')

arrServer=[[server1.price,server1.model,server1.year,server1.cdbay,server1.stype],
           [server2.price,server2.model,server2.year,server2.cdbay,server2.stype],
           [server3.price,server3.model,server3.year,server3.cdbay,server3.stype]]

print('''Виберіть, що бажаєте зробити:
1. - Вивести на екран всі ноутбуки
2. - Вивести на екран всі ПК
3. - Вивести на екран всі сервери
4. - Найти ноутбуки по параметру
5. - Найти ПК по параметру
6. - Найти сервери по параметру
7. - Вийти''')
while True:
    print("Введіть команду")
    command = input()
    if command == '1':
        laptop1.print()
        laptop2.print()
        laptop3.print()
    elif command == '2':
        pc1.print()
        pc2.print()
        pc3.print()
    elif command == '3':
        server1.print()
        server2.print()
        server3.print()
    elif command == '4':
        key1 = input("Введіть параметр для пошуку ноутбука: ")
        Product.search(arrLaptop,key1)
    elif command == '5':
        key2 = input("Введіть параметр для пошуку ПК: ")
        Product.search(arrPC,key2)
    elif command == '6':
        key3 = input("Введіть параметр для пошуку сервера: ")
        Product.search(arrServer,key3)
    elif command == '7':
        break
    else:
        print('Невідома команда')
