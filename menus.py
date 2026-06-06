import random
import readchar
import sys
import time
from colorama import Fore, Back, Style, init

grid = []
i = 5
gold = 0
height = 24
width = 30

player_x = 0
player_y = 0
#------------------------------------------------------------------------------------------------------------------------------------
def display_map():      #This is what displays the map
    time.sleep(.1)
    clear_screen()
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
    
    if player_y == height - 1:
        screen += Fore.GREEN + "Congratulations you won!\n"
    if i == 0:
        screen += Fore.RED + "Game Over! You lost all your life\n\n"
        print(screen, end="")
        sys.exit()
    else:
        screen += "                                 \n"
    print(screen, end="")
#------------------------------------------------------------------------------------------------------------------------------------
def generate_map():
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
#------------------------------------------------------------------------------------------------------------------------------------
def clear_screen():     #This clears the terminal before displaying the updated map to help reduce clutter
    print("\033[H", end="")
#------------------------------------------------------------------------------------------------------------------------------------
def inventory():
    clear_screen()
    screen = ""
    screen += "Hello"
    print(screen, end="")
    #------------------------------------------------------------------------------------------------------------------------------------