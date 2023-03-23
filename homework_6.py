#Есть класс Animal c одним методом voice().
#class Animal:
#def voice(self):
#pass
#1. Создать от него три класса наследника и для каждого сделать свою реализацию метода voice().
#2. Создать по одному экземпляру всех наследников и вызвать для каждого переопределенный метод voice().

class Animal:
    def voice(self):
        pass

class Animal_cat(Animal):
    def tom(self):
        print("help meee")

class Animal_dog(Animal):
    def bob(self):
        print("no help")
class Animal_horse(Animal):
    def ben(self):
        print("roleksy")

cat=Animal_cat()
cat.tom()
dog=Animal_dog()
dog.bob()
horse=Animal_horse()
horse.ben()
