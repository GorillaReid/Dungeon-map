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
height = 30
width = 35
empty = 0
level = 1
wlevel = 0

player_x = 0
player_y = 0
#------------------------------------------------------------------------------------------------------------------------------------
def display_map():      #This is what displays the map
    global empty
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
            elif char == "$":
                line += Fore.GREEN + Back.GREEN + "$$"
            elif char == " ":
                line += Back.WHITE + "  "
                empty += 1
        screen += line + "\n"
    screen += Back.RESET + Fore.RED + "Life: "
    
    life = ["!"] * i
    for x in range(len(life)):
        line = Back.LIGHTRED_EX + Fore.LIGHTRED_EX + "!!" + Back.BLACK + Fore.BLACK + "!"
        screen += line
    screen += "   " + Fore.LIGHTYELLOW_EX + Back.RESET + f"\n\nGold: {gold}\n" + Fore.CYAN + f"Use W,A,S,D to move\n{empty}\n"
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
        direction = random.choices(["down","left","right","up"], weights=[15, 40, 40, 5])[0]       #picks a random direction to generate the path

        if direction == "down":     #generates a path that goes down
            player_y += 1
        elif direction == "left" and player_x > 1 and player_y > 1:      #generates a path that goes left
            player_x -= 1
        elif direction == "right" and player_x < width - 2 and player_y > 1:     #generates a path that goes right
            player_x += 1
        elif direction == "up" and player_y > 1:        #generates a path that goes up (for more variety)
            player_y -= 1

    grid[height -1][player_x] = " "
    
    for y in range(height):                         #enemys
        for x in range(len(grid[y])):
            if grid[y][x] == " ":
                place = random.randint(1, 100)
                if place >= 95:
                    grid[y][x] = "!"

    for y in range(height):                         #gold
        for x in range(len(grid[y])):
            if grid[y][x] == " ":
                place = random.randint(1, 100)
                if place >= 95:
                    grid[y][x] = "%"

    for y in range(height):                         #keys
        for x in range(len(grid[y])):
            if grid[y][x] == " ":
                place = random.randint(1, 1000)
                if place > 999:
                    grid[y][x] = "$"
    return start_x
#------------------------------------------------------------------------------------------------------------------------------------
def new():     #This clears the terminal before displaying the updated map to help reduce clutter
    print("\033[H", end="")
#------------------------------------------------------------------------------------------------------------------------------------
def inventory():
    global wlevel
    clear()
    screen = ""
    if wlevel > 0:
        screen += f"Weapon Level: {wlevel}"
    else:
        screen = "You currently dont have anything in your inventory"
    print(screen, end="")
    time.sleep(1)
#------------------------------------------------------------------------------------------------------------------------------------
def move():
    global gold
    global i
    global level
    global empty
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
        if move == "m":
            gold += 100
        if move == "r":
            empty = 0
            generate_map()

        if grid[player_y][player_x] == "%":     #checks if the player is on a treasure item and gives them a random amount of gold between 1-5
            value = random.randint(1, 3)
            gold += value
        if grid[player_y][player_x] == "!":
            i -= 1
        grid[player_y][player_x] = "*"
        display_map()       #displays the map
        if player_y == height - 1:
            print(Fore.GREEN + f"You made it through Level {level}!\n")
            level += 1
        if i <= 0:
            print(Fore.RED + "Game Over! You lost all your life\n")
            sys.exit()
    time.sleep(1)
#------------------------------------------------------------------------------------------------------------------------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#------------------------------------------------------------------------------------------------------------------------------------
def shop():
    global gold
    global wlevel
    global i
    clear()
    print(Fore.RED + "Press the corresponding button to what you want to buy" + Fore.YELLOW + "\nGold: ", gold, Fore.LIGHTRED_EX + "\nL: Weapon Level\nM: Extra Life")
    shop = readchar.readkey().lower()

    if shop == "l":
        if gold >= 100:
            gold -= 100
            print(Fore.LIGHTBLUE_EX + "You have succsessfully upgraded your Weapon Level")
            wlevel += 1
        else:
            print(Fore.RED + f"You dont have enough gold for that, you need ", 100 - gold, Fore.RED + " more gold")
    if shop == "m":
        if gold >= 100:
            gold -= 100
            print(Fore.LIGHTBLUE_EX + "You have succsessfully bought another Life!")
            i += 1
        else:
            print(Fore.RED + f"You dont have enough gold for that, you need ", 100 - gold, Fore.RED + " more gold")
    time.sleep(1)
#------------------------------------------------------------------------------------------------------------------------------------