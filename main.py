import random       #imports for different libarys
import time
import sys
from colorama import Fore, Back , Style, init
import readchar
import menus

menus.generate_map()

player_x = menus.generate_map().start_x      #resets the players position back to the start
player_y = 0
menus.grid[player_y][player_x] = "*"      #tells the program to place a * at the players current position

menus.display_map()       #displays the map

while player_y != menus.height - 1:       #loop that runs until the player gets to the bottom of the map
    move = readchar.readkey().lower()
    menus.grid[player_y][player_x] = " "

    if move == "s" and player_y + 1 < menus.height and menus.grid[player_y + 1][player_x] != "#":       #checks if the play eneted s and moves them down if they did
        player_y += 1
    if move == "w" and menus.grid[player_y - 1][player_x] != "#":     #checks if the player entered w and moves them up if they did
        player_y -= 1 
    if move == "d" and menus.grid[player_y][player_x + 1] != "#":     #checks if the player entered d and moves them up if they did
        player_x += 1
    if move == "a" and menus.grid[player_y][player_x - 1] != "#":     #checks if the player entered a and moves them up if they did
        player_x -= 1
    if move == "i":
        menus.inventory()

    if menus.grid[player_y][player_x] == "%":     #checks if the player is on a treasure item and gives them a random amount of menus.gold between 1-5
        value = random.randint(1, 3)
        menus.gold += value
    if menus.grid[player_y][player_x] == "!":
        menus.i -= 1
    menus.grid[player_y][player_x] = "*"
    menus.display_map()       #displays the map