import random       #imports for different libarys
import time
import sys
from colorama import Fore, Back , Style, init
import readchar
import menus

while 1:

    print("Press Enter to play a second time")
    menu = readchar.readkey().lower()
    time.sleep(2)
    if menu == "i":
        while 1:
            menus.inventory()
    if menu == "k":
        menus.move()