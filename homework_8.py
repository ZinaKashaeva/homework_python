#Необходимо считать любой текстовый файл на вашем ПК (можно создать новый)
# и создать на его основе новый файл, где содержимое будет записано в обратном порядке.
# В конце программы вывести на экран оба файла -
#старый в неизменном виде и новый в обратном порядке.

with open('file_1.txt', 'w') as file1:
    file1.writelines('Homework 8')

with open('file_2.txt', 'w') as file2:
    for z in reversed(list(open('file_1.txt'))):
        words = z.split()
        reversed_words = ' '.join(reversed(words))
#        print(reversed_words)
    file2.writelines(reversed_words)

file = open("file_1.txt")
print(file.read())
file2 = open("file_2.txt")
print(file2.read())


