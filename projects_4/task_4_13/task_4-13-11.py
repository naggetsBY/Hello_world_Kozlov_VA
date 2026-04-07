OVarray = input("Введите числа через запятую:").split(', ')
summa = 0  

for i in range(len(OVarray)):
    if i % 2 == 0:  
        summa += int(OVarray[i])

print("Сумма элементов с четными индексами:", summa)