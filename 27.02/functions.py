'''
contacts = {
    'Аня' : {
        'мобільний': '050294754827',
        'робочий': '0672845343',
    },
    'Антон СТО': {
        'мобільний': None,
        'робочий': '05028758343',
    },  
    'Тимофій Карпати': {
        'мобільний': '0973848594',
        'робочий': None,
    }
}

action = int(input('1. знайти контакт\n2.продивитись всі контакти\n0.вихід'))
action = int(input('оберіть дію: '))
'''
'''
def print_greeting():
    print('====================')
    print('=== Hello, User! ===')
    print('====================')

def print_named_greeting(name: str = 'guest'):
    print('====================')
    print(f'=== Hello, {name.upper()}! ===')
    print('====================')


print_named_greeting()
print_named_greeting('Антон')
# print_greeting()
'''
'''
def my_sum(num1: float, num2: float) -> float:
    return num1 + num2

result = my_sum(10,12)
print(result)

def print_full_name(first_name: str, last_name: str):
    print(f'{last_name} {first_name}')

print_full_name(last_name='коваль', first_name='антон')
print_full_name('антон', 'коваль')

def print_my_animal(animal, name, age):
    print(f'i have {animal} {age} years old named {name}. ')


print_my_animal('dog', age=10, name='патрон')

def only_positional(name, /):
    print('Hello, ' + name)

# only_positional(name='Vova')
    
def only_key_word(*, name):
    print('Hello '+ name)

only_key_word(name='Vova')

print('data', 10, 'abc', sep=', ', end='!!!!!!!!!!!!!!!!')

'''
'''
def my_sum(*nums):
    result = 0
    for i in nums:
        result += i
    return result

print(my_sum(10, 12, 12))
print(my_sum(10, 12))
print(my_sum(210))
print(my_sum(10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10))

def my_function(**data):
    print(type(data))
    for key in data:
        print(f'{key}: {data[key]}')


# my_function(name='Vova', city='Odesa', job='Teacher')
        

def unpack_list(a, b, c):
    print(a, b, c, sep=', ')

my_list = [4, 5, 6]
unpack_list(*my_list)

def unpack_dictionary(fname,lname):
    print(fname, lname)


person = {
    'fname': 'антон',
    'lname': 'коваль'
}

unpack_dictionary(**person)
'''
'''
global_var = 16 # глобальна область видимості
def local_function(local_param):
    global global_var
    global_var = 10
    local_var = 10 # локальна область видимості
    print(local_param, local_var, global_var)

local_function(5)

print(global_var)
#print(local_var)
#print(local_param)
#print(local_var)
'''
'''
def enclosing_func():

    enclosing_var = 10
    def inner_func():
        print('hello from inner', enclosing_var)
    inner_func()

enclosing_func()

def do_something():
    print('doing some stuff...')


def main():
    print('start program...')
    do_something()
    print('end of program')

if __name__ == '__main__':
    main()
'''