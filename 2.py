from random import randint

a = int(input('Введите размер списка '))
list = []
list2 = []
for i in range(a):
    list.append(randint(0, 9))
for i in range(len(list)):
    while i < len(list)/2 and a > len(list)/2:
        a = a - 1
        a = list[i] * list[a]
        list2.append(a)
        i += 1
print(list)
print(list2)
