from list_functions import *
import random

array = []
elment_to_find = random.randint(0,100)
for i in range(0,10):
    array.append(random.randint(0,100))
    
print(array)
print(Sort(array,1))
print(elment_to_find)
print(find_element(str(elment_to_find) ,array))
print(find_element_raw(array))
print(arithmetic_mean_float(array))
print(first_five_min(array))
print(first_five_max(array))

array = []
for i in range(0,10):
    array.append(random.randint(0,100))
print(array)
print(filtr_same_elements(array)) 
