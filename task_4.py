revenue = int(input("Введите сумму выручку вашей фирмы: "))
costs = int(input("Введите сумму издержек: "))
staff = int(input("Введите численность сотрудников фирмы: "))
if revenue > costs:
    profit = revenue - costs
    profitability = costs / revenue
    profit_p_person = profit / staff
print(f'Прибыль: {profit}')
print(f'Рентабльность: {profitability}')
print(f'Прибыль фирмы в расчете на одного сотрудника: {profit_p_person}')
