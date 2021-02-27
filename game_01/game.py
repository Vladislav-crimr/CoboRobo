import time
import random


comp = you = 0
name = input(" Вебите имя ")

def kub(par,name):
    rand = random.randint(1,6)
    rand2 = random.randint(1,6)
    par += rand + rand2
    time.sleep(2)
    print(name + " Выбил " + str(rand + rand2) + " очков ")
    return par


while (comp < 66) or (you < 66):
    comp = kub(comp, " компютер ")
    you = kub(you, name)

if you < comp:
    print(" Победил компютер ")
else:
    print(" Победил " + name)


print(" Компютер победил " + str(comp) + ' очков ')
print(name + " победил " + str(you) + ' очков ')