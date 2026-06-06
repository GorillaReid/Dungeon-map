import random       #imports for different libarys
import time
import sys
import os
from colorama import Fore, Back , Style, init
import readchar

init(autoreset=True)    #This automaticly resets the text color after each print

def clear_screen():     #This clears the terminal before displaying the updated map to help reduce clutter
    os.system('cls' if os.name == 'nt' else 'clear')

def display_map():      #This is what displays the map
    clear_screen()
    for row in grid:
        line = ""
        for char in row:
            if char == "#":
                line += Fore.LIGHTBLACK_EX + Back.LIGHTBLACK_EX + "##"
            elif char == "*":
                line += Fore.BLUE + Back.BLUE + "**"
            elif char == "%":
                line += Fore.YELLOW + Back.YELLOW + "%%"
            elif char == "!":
                line += Fore.RED + Back.RED + "!!"
            else:
                line += Back.WHITE + "  "
        print(line)

grid = []       #Declaring some int and var for the first time
gold = 0
width = 30
height = 24
timeout = 5

start_time = time.time()    #used to help prevent the map from taking to long to generate

for y in range(height):     #generates the base structure of the map
    row = ["#"] * width
    grid.append(row)

start_x = random.randint(2, width - 3)      #picks a random spot on the top row to start the player at

player_x = start_x      #setting the players starting position
player_y = 0

while player_y < height - 1:    #loop runs until the path generation reaches the bottom
    if time.time() - start_time > timeout:      #Runs if the map takes to long to generate
        sys.exit("Map generation timed out. Try again")

    grid[player_y][player_x] = " "
    direction = random.choices(["down","left","right","up"], weights=[20, 30, 30, 20])[0]       #picks a random direction to generate the path

    if direction == "down":     #generates a path that goes down
         player_y += 1
    elif direction == "left" and player_x > 1:      #generates a path that goes left
         player_x -= 1
    elif direction == "right" and player_x < width - 2:     #generates a path that goes right
        player_x += 1
    elif direction == "up" and player_y > 1:        #generates a path that goes up (for more variety)
        player_y -= 1

grid[height -1][player_x] = " "     #generates a path at the bottom

treasure = []
for y in range(height):
    for x in range(len(grid[y])):
        if grid[y][x] == " ":
            treasure.append(x)

    treasure_amount = len(treasure) // random.randint(50, 100)
    chosen = random.sample(treasure, treasure_amount)
    for place in chosen:
        if grid[y][place] == " ":
            grid[y][place] = "%"

enemy = []
for y in range(height):
    for x in range(len(grid[y])):
        if grid[y][x] == " ":
            enemy.append(x)

    enemy_amount = len(enemy) // random.randint(50, 100)
    chosen = random.sample(enemy, enemy_amount)
    for place in chosen:
        if grid[y][place] == " ":
            grid[y][place] = "!"

player_x = start_x      #resets the players position back to the start
player_y = 0
grid[player_y][player_x] = "*"      #tells the program to place a * at the players current position

display_map()       #displays the map

while player_y != height - 1:       #loop that runs until the player gets to the bottom of the map
    print("Gold: ", gold, "\nw = up, s = down, d = right, a = left: ")     #displays a prompt for the user and accepts input from them
    move = readchar.readkey().lower()
    grid[player_y][player_x] = " "

    if move == "s" and player_y + 1 < height and grid[player_y + 1][player_x] != "#":       #checks if the play eneted s and moves them down if they did
        player_y += 1
    if move == "w" and grid[player_y - 1][player_x] != "#":     #checks if the player entered w and moves them up if they did
        player_y -= 1 
    if move == "d" and grid[player_y][player_x + 1] != "#":     #checks if the player entered d and moves them up if they did
        player_x += 1
    if move == "a" and grid[player_y][player_x - 1] != "#":     #checks if the player entered a and moves them up if they did
        player_x -= 1

    if grid[player_y][player_x] == "%":     #checks if the player is on a treasure item and gives them a random amount of gold between 1-5
        value = random.randint(1, 3)
        gold += value
    grid[player_y][player_x] = "*"
    display_map()       #displays the map

    if player_y == height - 1:      #checks if the player reached the bottom, if so it tells them they won and the program ends (for now)
        print("Congratulations you won!")