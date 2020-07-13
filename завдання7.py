class Student:
    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.labs = [0] * self.conf.get('lab_num')
        self.work = 0.0
 
    def make_lab(self, m, n=-1):         #задати к-сть виконаних лаб
 
        if n >= self.conf.get('lab_num'):
            return self
 
        if n == -1:
            try:
                n = self.labs.index(0)
            except:
                return self
 
        if m > self.conf.get('lab_max'):
            m = self.conf.get('lab_max')
 
        self.labs[n] = m 
        #print(self.labs)
 
        return self
 
 
    def make_work(self, m):             #виконати творчу роботу
        if m > self.conf.get('work_max'):
            m = self.conf.get('work_max')
        self.work = m
        return self
 
    def is_certified(self):             #чи виконав достатню к-сть робіт
        smarks = sum(self.labs) + self.work
        
        if smarks/100 >= self.conf.get('k'):
            is_cert = True
        elif smarks/100 < self.conf.get('k'):
            is_cert = False
        return (smarks, is_cert)

conf = {'work_max': 25,'lab_max': 30,'lab_num': 2,'k': 0.5}  #словник з налаштуваннями курсу

stud1 = Student('Andriyko', conf)
print('Студент',stud1.name,'Отримав 60% всіх балів:',stud1.is_certified()) 
stud2 = Student('Ivanko', conf)
stud2.make_lab(60).make_lab(35.2)                            #виконати лаби на задану к-сть балів
print('Студент',stud2.name,'Отримав 60% всіх балів:',stud2.is_certified()) 
stud3 = Student('Sergiyko', conf)
stud3.make_lab(10).make_lab(10).make_work(15)                #виконати лаби та роботу на задану к-сть балів
print('Студент',stud3.name,'Отримав 60% всіх балів:',stud3.is_certified()) 

