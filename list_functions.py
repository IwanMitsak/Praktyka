def Sort(array, mod):
    """ Сортує елементи взалежності від моду. 1 сортує за зростаням 2 за спаданням """
    Run = True

    if mod == 1:
        while Run:
            Run = False
            for i in range(0,len(array)-1):
                if array[i] > array[i+1]:
                    help_ = array[i]
                    array[i] = array[i+1]
                    array[i+1] = help_
                    Run = True
    elif mod == 2:
        while Run:
            Run = False
            for i in range(0,len(array)-1):
                if array[i] < array[i+1]:
                    help_ = array[i] 
                    array[i] = array[i+1]
                    array[i+1] = help_
                    Run = True

    return array

def find_element(elment_to_find, array):
    """ Шукає елемент в масиві """
    try:
        return array.index(elment_to_find)
    except:
        return None

def find_element_raw(array):
    """ Шукає послідовність елементів """
    return array

def first_five_min(array):
    """ Шукає 5 найменших елементів масиву """
    five_min = []
    for i in range(0,5):
        five_min.append(min(array))
        del array[array.index(min(array))]

    return five_min

def first_five_max(array):
    """ Шукає 5 найбільших елементів масиву """
    five_max = []
    for i in range(0,5):
        five_max.append(max(array))
        del array[array.index(max(array))]

    return five_max

def arithmetic_mean_float(array):
    """ Шукає середнє арефметичне списку """
    sum_n = float(0)
    length = len(array)
    for n in array:
        sum_n = float(n)
    try:
        return sum_n / length
    except ZeroDivisionError:
        return 0
    
def filtr_same_elements(array):
    """ Повертає список без повторень елементів """
    return list(dict.fromkeys(array)) 
