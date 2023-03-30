# Необходимо дополнить "Практическое задание №6" таким образом, чтобы в конце программы
# мы вызвали статический метод родительского класса Animal,
# который вывел бы нам количество всех созданных экземпляров.
# Если мы создали трех наследников в предыдущем задании, то наш метод должен вывести на экран число 3.

class Animal:
    counts = 0

    def voice(self):
        pass

    def __init__(self):

        Animal.counts = Animal.counts+1


class Animal_cat(Animal):
    def voice(self):
        print("help meee")


class Animal_dog(Animal):
    def voice(self):
        print("no help")


class Animal_horse(Animal):
    def voice(self):
        print("roleksy")


def count_instance():
    print("Всего: ", Animal.counts)


cat = Animal_cat()
cat.voice()
dog = Animal_dog()
dog.voice()
horse = Animal_horse()
horse.voice()
count_instance()
