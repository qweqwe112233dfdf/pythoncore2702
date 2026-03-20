'''
try:
    number = float(input('enter number: '))
    # raise Exception('arg1')
    print(number)
except ValueError as ex:
    print('value error', ex.args[0])
'''

file_path = 'demo.txt'
'''
file = open(file_path, '+a')

file.close()
'''
#with open(file_path, 'a') as file:
#    print('file created successfully!')

file_path = './test_files/test.txt'
'''
with open(file_path, 'r') as f:
    file_content = f.read()
    print(file_content)
    print(type(file_content))

with open(file_path, 'r') as f:
    line_1 = f.readline().strip()
    print(line_1)
    line_2 = f.readline().strip()
    print(line_2)
''' '''
with open(file_path, 'r') as f:
    for line in f:
        print(line.strip())

with open(file_path, 'r') as f:
    lines = f.readlines()
    print(lines)
'''
with open(file_path, 'w') as f:
    f.write('\nthis data is written by code\n')
    f.writelines(['line1\n', 'line2\n', 'line3\n'])

try:
    with open('demo6.txt', 'x'):
        print('file created successfully')
except FileExistsError:
    print('file already exists!')