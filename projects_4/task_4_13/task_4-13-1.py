print("Введите 4 числа по очереди:")

z = float(input("Введите первое число:")) 
o = float(input("Введите второе число:")) 
n = float(input("Введите третье число:")) 
a = float(input("Введите четвертое число:")) 

if z < o:
    min_value = z
else: 
    min_value = o

if n < a :
    min_value1 = n
else: 
    min_value1 = a

if min_value < min_value1:
    print("Минимальное из четырех чисел:", min_value)
else:
    print("Минимальное из четырех чисел:", min_value1)