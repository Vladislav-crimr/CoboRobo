import time
import random

hpuser = 0
hpshot = 50
key = 0 
coins = 0


# появляется стражник и стреяет по тебе и наносит урон
def guard(hpuser,hpshot):
    print(" ты видиш стражникак ")
    hpuser = hpuser - hpshot
    print(" от тебе наносит 50 урона")
    return hpuser

def chase(key, hpuser, coins):
    print(" ты видиш сундук тебе выподает ")
    randChase = random.randint(1,3)
    if randChase == 1:
        key = key + 1
        print(" ключ")
    elif randChase == 2:
        hpuser = hpuser + 30
        print(" 30 хп")
    elif randChase == 3:
        coins = coins + 30 
        print(" 30 монет")

    resuit = {"key": key, "hpuser": hpuser, "coins": coins}
    key = hpuser = coins = 0
    return resuit


# name = input(" Привет как тебя зовут? ")
# print(name + ''' ты проволился в подвал и тебе нужно дойти до конца.
# Но когда ты будеш тити ты встретиш комнаты.
# ты можеж в них ити или не ити.
# Но перед последней комнаты будет стоять продовец.
#  но за ним стоит зокрытая дверь. ''')
# user = int(input(" Ты идёш и встречяеш комнату нажми (1 если да или 2 еслши нет) "))
# if user == 1:
#     roomOne = random.randint(1,2)
#     if roomOne == 1:
#         hpuser = guard(hpuser,hpshot)
#         print(" у тебя осталось " + str(hpuser) + " hp")
#     else:
#         chase(key, hpuser, coins)
# elif user == 2:
#     pass
# elif user == '':
#     print(" неверное число ")
# while True:
    # roomOne = guard(hpuser,hpshot)
    # hpuser = roomOne
    # if hpuser > 0:
    #     print('Ты еще жив и идешь в следующую комнату')
    # else:
    #     print(" Ты сдох ")
    #     break
while True:
    roomOne = chase(key, hpuser, coins)
    key += roomOne['key']
    print(key)
    coins += roomOne['coins']
    print(coins)
    hpuser += roomOne['hpuser']
    print(hpuser)
    if hpuser > 200:
        break