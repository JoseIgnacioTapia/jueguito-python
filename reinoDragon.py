import random
import time


def introduccion():
    print("Estamos en una tierra llena de dragones.Delante de nuestro,\nse ven dos cuevas. En una cueva, el dragon amigable")
    print("y compartira el tesoro contigo. El otro dragon \nes codicioso y hambriento, y te va a comer ni bien te vea.")
    print("")


def cambiarCueva():
    introduccion()
    cueva = ""
    while cueva != "1" and cueva != "2":
        print("Ha que cueva quieres entrar 1 o 2?")
        cueva = input()

    return cueva


newGame = "s"
oro = 0

while newGame == "s":

    numCueva = cambiarCueva()

    print("Te acercas a la cueva")
    time.sleep(2)
    print("Esta oscuro y tenebroso")
    time.sleep(2)
    print("Un gran dragon salta delante tuyo y...")
    time.sleep(2)

    friendlyCueva = random.randint(1, 2)

    if numCueva == str(friendlyCueva):
        print("Te entrega el tesoro...")
        cofre = random.randint(50, 200)
        print("Has ganado " + str(cofre) + " en oro")
        oro += cofre
    else:
        print("El dragon te come de un bocado...")
        print("Perdiste!!\nOro acumulado:", oro)

    newGame = input("Quieres jugar de nuevo?")

print('GAME OVER')