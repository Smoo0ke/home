a = int(input('Введите число: '))
b = [1,-1]
c = [1,1]

for i in range(2,n):
    list = c[i-1]+c[i-2]
    c.append(list)
    list2 = b[i-2] - b[i-1]
    b.append(list2)

b.reverse()
v.insert(0, 0)

print(' Для {a} => {b+c}')
