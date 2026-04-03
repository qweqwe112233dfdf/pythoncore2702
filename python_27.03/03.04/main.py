from characters import *
from enemies import *

# enemies
grob = goblin('grob', 10, 30)
dracula = Vampire('dracula', 12, 40)

#players
boris = Fighter('Boris', 15, 50)
anna = Healer('anna', 7, 35)

print('--- Stats before fight ---')
print(grob, dracula, boris, anna, sep='\n')


# enemies turn
grob.attack(boris)
dracula.attack(boris)

# players turn
boris.attack(dracula)
anna.heal(boris)

# enemies turn
grob.attack(anna)
dracula.lifesteal(anna)

print('--- Stats after fight ---')
print(grob, dracula, boris, anna, sep='\n')