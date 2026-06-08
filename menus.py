import random
import readchar
import sys
import time
import os
from colorama import Fore, Back, Style, init

init(autoreset=True)

grid = []
i = 5
gold = 0
height = 24
width = 30
empty = 0

player_x = 0
player_y = 0
#------------------------------------------------------------------------------------------------------------------------------------
def display_map():      #This is what displays the map
    time.sleep(.1)
    new()
    screen = ""
    for row in grid:
        line = ""
        for char in row:
            if char == "#":
                line += Fore.LIGHTBLACK_EX + Back.LIGHTBLACK_EX + "##"
            elif char == "*":
                line += Fore.BLUE + Back.BLUE + "**"
            elif char == "%":
                line += Fore.LIGHTYELLOW_EX + Back.LIGHTYELLOW_EX + "%%"
            elif char == "!":
                line += Fore.RED + Back.RED + "!!"
            elif char == " ":
                line += Back.WHITE + "  "
        screen += line + "\n"
    screen += Back.RESET + Fore.RED + "Life: "
    
    life = ["!"] * i
    for x in range(len(life)):
        line = Back.LIGHTRED_EX + Fore.LIGHTRED_EX + "!!" + Back.BLACK + Fore.BLACK + "!"
        screen += line
    screen += "   " + Fore.LIGHTYELLOW_EX + Back.RESET + f"\n\nGold: {gold}\n" + Fore.CYAN + "Use W,A,S,D to move\n\n"
    print(screen, end="")
#------------------------------------------------------------------------------------------------------------------------------------
def generate_map():
    global grid
    global empty
    grid = []
    for y in range(height):     #generates the base structure of the map
        row = ["#"] * width
        grid.append(row)

    start_x = random.randint(2, width - 3)      #picks a random spot on the top row to start the player at

    player_x = start_x      #setting the players starting position
    player_y = 0

    while player_y < height - 1:    #loop runs until the path generation reaches the bottom

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

    grid[height -1][player_x] = " "
    
    empty = 0
    enemy = []
    for y in range(height):
        enemyr = []
        for x in range(len(grid[y])):
            if grid[y][x] == " ":
                enemyr.append(x)
                empty += 1
        enemy.append(enemyr)

    enemy_amount = empty // random.randint(20, 50)
    for z in range(enemy_amount):
        possible_rows = [y for y in range(height) if enemy[y]]
        if not possible_rows:
            break
        y = random.choice(possible_rows)
        x = random.choice(enemy[y])
        if grid[y][x] == " ":
            grid[y][x] = "!"
            enemy[y].remove(x)

    treasure = []
    for y in range(height):
        for x in range(len(grid[y])):
            if grid[y][x] == " ":
                treasure.append(x)

        treasure_amount = len(treasure) // (enemy_amount * 10)
        chosen = random.sample(treasure, treasure_amount)
        for place in chosen:
            if grid[y][place] == " ":
                grid[y][place] = "%"
    return start_x
#------------------------------------------------------------------------------------------------------------------------------------
def new():     #This clears the terminal before displaying the updated map to help reduce clutter
    print("\033[H", end="")
#------------------------------------------------------------------------------------------------------------------------------------
def inventory():
    clear()
    print("WIP")
    time.sleep(1)
#------------------------------------------------------------------------------------------------------------------------------------
def move():
    global gold
    global i
    player_x = generate_map()      #resets the players position back to the start
    player_y = 0
    grid[player_y][player_x] = "*"
    display_map()

    while player_y != height - 1:       #loop that runs until the player gets to the bottom of the map
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
        if grid[player_y][player_x] == "!":
            i -= 1
        grid[player_y][player_x] = "*"
        display_map()       #displays the map
        if player_y == height - 1:
            print(Fore.GREEN + "Congratulations you won!\n")
        if i <= 0:
            print(Fore.RED + "Game Over! You lost all your life\n")
            sys.exit()
    time.sleep(1)
#------------------------------------------------------------------------------------------------------------------------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#------------------------------------------------------------------------------------------------------------------------------------
def shop():
    clear()
    print(Fore.RED + "Press the corresponding button to what you want to buy" + Fore.YELLOW + "\nGold: ", gold, Fore.LIGHTRED_EX + "\nH: health potion")
    shop = readchar.readkey().lower()

    if shop == "h":
        if gold >= 100:
            print("yay")
        else:
            print("nah")
        time.sleep(1)
#------------------------------------------------------------------------------------------------------------------------------------