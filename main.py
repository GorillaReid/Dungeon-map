import random       #imports for different libarys
import time
import sys
from colorama import Fore, Back , Style, init
import readchar
import menus

while 1:
    menus.clear()
    print(Fore.BLUE + "Press the corresponding button to what you want to do:" + Fore.LIGHTBLUE_EX + "\nL: Enter a Dungeon\nI: Open your inventory\nJ: Open the Shop")
    menu = readchar.readkey().lower()
    time.sleep(1)
    if menu == "i":
        menus.inventory()
    if menu == "l":
        menus.move()
    if menu == "j":
        menus.shop()