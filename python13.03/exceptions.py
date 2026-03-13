'''
my_list = ['orange', 'apple', 'banana']

#print(my_list[10])

#print(10 / 0)

def recursion():
    recursion()

var = recursion()

# var()
'''
operators = ['+', '-', '*', '/']

while(True):
    try: 
        num1 = float(input('enter first number: '))
        num2 = float(input('enter second number: '))
        action = input('enter operation: ')
        if action not in operators:
            raise Exception(action)

        match action:
            case '+': print(f'{num1} + {num2} = {num1 + num2}')
            case '-': print(f'{num1} - {num2} = {num1 - num2}')
            case '*': print(f'{num1} * {num2} = {num1 * num2}')
            case '/': print(f'{num1} / {num2} = {num1 / num2}')
    except ZeroDivisionError:
        print('не можна ділити на нуль!')
    ''' except ValueError:
        print('некоректне число!')
    except Exception as ex:
        print(f'некоректна операція! {ex.args[0]}') '''
    finally:
        repeat = input('continue? Y/N ')
        if repeat.lower() == 'n':
            break