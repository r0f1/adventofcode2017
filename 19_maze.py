def handle_plus(maze, direction, x, y):
    n, e, s, w = maze[y-1][x], maze[y][x+1], maze[y+1][x], maze[y][x-1]

    if direction in ("N", "S"):
        if e == " ": return x-1, y, "W"
        else:        return x+1, y, "E"
    elif direction in ("E", "W"):
        if n == " ": return x, y+1, "S"
        else:        return x, y-1, "N"

def walk(maze, direction, x, y):
    if   direction == "N": y -= 1
    elif direction == "E": x += 1
    elif direction == "S": y += 1
    elif direction == "W": x -= 1
    return x, y

with open("19_input.txt") as f:
    maze = f.readlines()

y = 0
x = maze[y].index("|")
direction = "S"
steps = 0

while maze[y][x] != " ":
    steps += 1
    x, y = walk(maze, direction, x, y)

    if maze[y][x] in ("|", "-"): 
        continue
    elif maze[y][x] == "+":
        x, y, direction = handle_plus(maze, direction, x, y)
        steps += 1
    else:
        print(maze[y][x])

print(steps)