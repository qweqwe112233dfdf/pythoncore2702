'''
try:
    number = float(input('enter number: '))
    # raise Exception('arg1')
    print(number)
except ValueError as ex:
    print('value error', ex.args[0])
'''

