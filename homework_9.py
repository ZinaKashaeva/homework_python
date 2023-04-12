#Необходимо создать два параллельных потока, каждый из которых выводил бы на экран
# числа от 10 до 1 в обратном порядке с интервалом в одну секунду.
#В выводе должно быть понятно какая нить выполняется, и когда каждая из них
# начинает и заканчивает своё выполнение.


import threading
import time


def function(interval):
    for n in range(10, 0,-1):
        print(f"Время: {time.ctime()}", f.name,  n)
        time.sleep(interval)


def function_2(interval):
    for n in range(10, 0,-1):
        print(f"Время: {time.ctime()} ", t.name,  n)
        time.sleep(interval)


f = threading.Thread(target=function, name="поток 1", args=(1, ))
t = threading.Thread(target=function_2, name="поток 2", args=(1, ))
f.daemon = True
t.daemon = True
f.start()
t.start()
f.join()
t.join()