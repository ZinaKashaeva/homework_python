#Есть список numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
#Вывести все нечетные числа больше 50, используя функцию filter().

numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
def num(in_num):
    if((in_num % 2) != 0) and (in_num > 50):
        return True
    else:
        return False


filter_num = filter(num, numbers)
print(list(filter_num))