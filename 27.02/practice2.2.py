def print_odd_numbers(start, end):
    min_num = min(start, end)
    max_num = max(start, end)

    print(f'непарні числа між {min_num} та {max_num}: ')
    for num in range(min_num, max_num + 1):
        if num % 2 != 0:
            print(num)
print_odd_numbers(10, 20)