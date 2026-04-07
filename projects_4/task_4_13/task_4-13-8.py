ListA = input("Введите числа через запятую:").split(', ')
count = 0
i = 0

for i in ListA:
    if int(i) > 0:
        count += 1
print("Количество положительных чисео:", count)