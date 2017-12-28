import numpy as np

class Grid():
    def __init__(self, lines, part):
        self.grid = np.array([[part if c == "#" else 0 for c in l] for l in lines])
        m = len(lines) // 2
        self.dimx = len(lines)
        self.dimy = len(lines)
        self.pos = (m, m)
        self.direction = 0

    def turn(self, part):
        x, y = self.pos
        if part == 1:
            if self.grid[y][x] == 0: self.direction = (self.direction - 1) % 4
            else:                    self.direction = (self.direction + 1) % 4
        else:
            if   self.grid[y][x] == 0: self.direction = (self.direction - 1) % 4
            elif self.grid[y][x] == 2: self.direction = (self.direction + 1) % 4
            elif self.grid[y][x] == 3: self.direction = (self.direction + 2) % 4

    def clean_or_infect(self, part):
        x, y = self.pos
        v = self.grid[y][x]
        if part == 1:
            v = (v+1) % 2 # 0=clean, 1=infected
        else:
            v = (v+1) % 4 # 0=clean, 1=weakened, 2=infected, 3=flagged
        self.grid[y][x] = v
        if part == 1 and v == 1: return 1
        if part == 2 and v == 2: return 1
        return 0

    def move(self):
        x, y = self.pos
        if   self.direction == 0: new_pos = (x, y-1)
        elif self.direction == 1: new_pos = (x+1, y)
        elif self.direction == 2: new_pos = (x, y+1)
        elif self.direction == 3: new_pos = (x-1, y)

        x, y = new_pos
        if x < 0 or x == self.dimx or y < 0 or y == self.dimy:
            if x < 0:
                self.pos = (0, y)
                self.dimx += 1
                new_grid = np.zeros((self.dimy, self.dimx))
                new_grid[:, 1:] = self.grid
            elif x == self.dimx:
                self.pos = (x, y)
                self.dimx += 1
                new_grid = np.zeros((self.dimy, self.dimx))
                new_grid[:, :-1] = self.grid
            elif y < 0:
                self.pos = (x, 0)
                self.dimy += 1
                new_grid = np.zeros((self.dimy, self.dimx))
                new_grid[1:, :] = self.grid
            elif y == self.dimy:
                self.pos = (x, y)
                self.dimy += 1
                new_grid = np.zeros((self.dimy, self.dimx))
                new_grid[:-1, :] = self.grid
            self.grid = new_grid
        else:
            self.pos = new_pos

    def __repr__(self):
        res = ""
        for y, line in enumerate(self.grid):
            for x, c in enumerate(line):
                if   c == 0: d = "."
                elif c == 1: d = "W"
                elif c == 2: d = "#"
                elif c == 3: d = "F"
                # d = "." if c == 0 else "#"
                if self.pos == (x,y): res += "[%s]" % d
                else:                 res += " %s " % d
            res += "\n"
        return res

with open("22_input.txt") as f:
    lines = [l.strip() for l in f]

for part, iterations in ((1, 10_000), (2, 10_000_000)):
    g = Grid(lines, part)
    i = 0
    for _ in range(iterations):
        g.turn(part)
        i += g.clean_or_infect(part)
        g.move()

    print(i)