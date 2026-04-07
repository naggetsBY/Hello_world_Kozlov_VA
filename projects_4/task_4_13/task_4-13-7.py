array = input("Введите числа через запятую:").split(', ')
sum = 0

for i in array:
    sum += int(i)

sa = sum // len(array)

print("Среднее арифметическое ваших числе:", sa)