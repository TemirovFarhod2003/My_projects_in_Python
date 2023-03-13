value =int(input("Введите целое положительное число: "))
sum_value = 0
if 99 < value < 1000:
    a = value // 100
    b = value // 10 % 10
    c = value % 10
    print(a + b + c)
