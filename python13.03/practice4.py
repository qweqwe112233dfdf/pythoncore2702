try:
    summa = float(input('яку суму зняти: '))
    card = 10000
    if summa // 10 == 0 and summa <= card:
        print(f'виводжу {summa}')
except ValueError:
    print('помилка')
    raise Exception('некоректна сума для зняття')
finally:
    print(f'завершення транзакції')
