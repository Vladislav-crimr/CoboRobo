import random
def fride():
    fride = int(input(" Вы хотите открыть холодильник 1-да 2-нет "))
    if fride == 1:
        mom()
    else:
        print(" конец игры ")     


def mom():
    randMom = random.randint(1,1000)
    if randMom <= 500:
        print(" Ты пел дошик и ты наелся пишей богов")
    else:
        alarm()


def alarm():
    alarm = int(input(" сработала сигнализацыя ты можеш спрятотся или остаться 1-остаться 2-спрятотся "))
    if alarm == 1:
        print(" пришла мать выпорела тебя и ты пошол спать голодный ")
    else:
        dad()


def dad():
    randDad = random.randint(1,1000)
    if randDad <= 500:
        print(" ты попытался спрятотся в туалет но там сидит батя")
    else:
        fride()


fride()