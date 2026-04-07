N = int(input("Введите количество чисел N: "))

sqr_sum = 0
for i in range(1, N + 1):
    sqr_sum += i ** 2

print("Сумма квадратов первых", N, "чисел равна:", sqr_sum)