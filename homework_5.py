#Есть список numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
#Используя модуль random, вывести случайный элемент этого списка.

import random
#print(dir(random))

numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
print("Выбранное число из списка = ", random.choice(numbers))