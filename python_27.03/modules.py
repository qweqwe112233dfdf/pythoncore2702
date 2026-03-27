import random

# from random import *

# from random import randint

# randint = 10

# print(randint(10, 14))
# print(randrange(10, 18, 2)) # 10 12 14 16

print(random.random()) # випадкове число від 0.0 до 1.0

if random.random() >= 0.9:
    print('heads')
else:
    print('tails')

print(random.uniform(10.5, 20.6))

fruits = ['apple', 'banana', 'orange', 'pineapple', 'mango']
print(random.choice(fruits))
weights = [0.1, 0.5, 0.1, 0.1, 0.2]
print(random.choices(fruits, weights=weights, k=3))
print(random.sample(fruits, k=3))

fruits.sort()
print(fruits)

random.shuffle(fruits)
print(fruits)