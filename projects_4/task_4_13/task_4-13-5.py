N = input("Введите необходимые данные:")

max = N[0]

for num in N:
    if max < num:
        max = num

print(max)