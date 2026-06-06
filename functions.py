import random

grid = []
gold = 0
for y in range(12):
    row = []
    row.append(random.choice(["#"]))
    for x in range(28):
        row.append(random.choice(["#","#","#"," "," ","%"]))
    row.append(random.choice(["#"]))
    grid.append(row)
row = []
for d in range(30):
    row.append(random.choice(["#"]))
grid.append(row)

starting  = []

for x in range(len(grid[0])):
    if grid[0][x] == " ":
        starting.append(x)

start_x = random.choice(starting)

grid[0][start_x] = "*"

player_x = start_x
player_y = 0

if grid[player_y + 1][player_x] == "#":
    grid[player_y + 1][player_x] = " "
while 1:
    amount = random.randint(1, 2)
    grid[player_y + amount][player_x] = "P"
    direction = random.randint(1, 2)
    if direction == 1:
        amount = random.randint(1, 3)
        grid[player_y][player_x - amount] = "P"
    if direction == 2:
        amount = random.randint(1, 3)
        grid[player_y][player_x + amount] = "P"
    if grid[player_y][player_x] == grid[1][2]:
        break
    break

for row in grid:
    print("".join(row))

while 1:
    print("Gold: ", gold)
    move = input("w = up, s = down, d = right, a = left: ").lower()
    grid[player_y][player_x] = " "

    if move == "s" and grid[player_y + 1][player_x] != "#":
        player_y += 1
    if move == "w" and grid[player_y - 1][player_x] != "#":
        player_y -= 1 
    if move == "d" and grid[player_y][player_x + 1] != "#":
        player_x += 1
    if move == "a" and grid[player_y][player_x - 1] != "#":
        player_x -= 1
    if grid[player_y][player_x] == "%":
        value = random.randint(1, 5)
        gold += value
    if grid[player_y][player_x] == "e":
        print("Test")

    grid[player_y][player_x] = "*"

    for row in grid:
        print("".join(row))