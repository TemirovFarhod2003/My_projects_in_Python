some_number = "456960"
if 99999<int(some_number)<999999:
    a = int(some_number[:3])
    b = int(some_number[-3:])
    sum_value_a = 0
    sum_value_b = 0
    while a > 0:
        digit = a % 10
        sum_value_a += digit
        a = a // 10
        digit1 = b % 10
        sum_value_b += digit1
        b = b // 10
    if sum_value_a == sum_value_b:
        print ("Ваш билет является счастливым")
    else:
        print ("Ваш билет обычный")
else:
    print("Номер билета введен некорректно")