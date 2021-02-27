import random

mySelf = True
def fride():
    global mySelf
    if mySelf == True:
        fride = int(input(" Вы хотите открыть холодильник 1-да 2-нет "))
        if fride == 1:
            mom()


def mom():
    randMom = random.randint(1,1000)
    if randMom <= 500:
        print(" Ты пел дошик и ты наелся пишей богов")
    else:
        alarm()

def alarm():
    global mySelf
    alarm = int(input(" сработала сигнализацыя ты можеш спрятотся или остаться 1-остаться 2-спрятотся "))
    if alarm == 1:
        print(" пришла мать выпорела тебя и ты пошол спать голодный ")
        mySelf = False
    else:
        dad()


def dad():
    global mySelf
    randDad = random.randint(1,1000)
    if randDad <= 500:
        print(" ты попытался спрятотся в туалет но там сидит батя")
        mySelf = False
    else:
        fride()


def end():
    global mySelf
    end = int(input(" Ты хочеш сыграть ещё раз 1-да , 2-нет "))
    if end == 1:
        mySelf = True
    else:
        mySelf = False

while mySelf:
    fride()
    end()
