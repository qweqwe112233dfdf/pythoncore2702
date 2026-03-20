def draw_line(length, direction, symbol):
    if direction == 'h':
        print(symbol * length)
    elif direction == 'v':
        for _ in range(length):
            print(symbol)
    else:
        print('помилка')
print('горизонтальна лінія: ')
draw_line(10, 'h', '=')

print('вертикальна лінія: ')
draw_line(5, 'v', '*')