Zarray = input("Введите числа через запятую:").split(', ')
sum = 0

for i in range(len(Zarray)):
    if i % 2 != 0:
        sum += int(Zarray[i])

print("Сумма элементов с нечетными индексами:", sum)