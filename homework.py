a =92, 3, 6, 10, 12, 16, 50
print(a)
b = 0
for i in range(1, len(a), 2):
    if i % 2 == 1:
        b += a[i]       
print(a ,"-> сумма элементов на нечётных позициях:", b)