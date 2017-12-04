import itertools
from collections import defaultdict

def move_right(x,y): return x+1, y
def move_down(x,y):  return x,y-1
def move_left(x,y):  return x-1,y
def move_up(x,y):    return x,y+1

def spiral(end):
    m = itertools.cycle([move_right, move_up, move_left, move_down])
    n = 1
    pos = 0,0
    times_to_move = 1

    yield n, pos

    while True:
        for _ in range(2):
            move = next(m)
            for _ in range(times_to_move):
                if n >= end:
                    return
                pos = move(*pos)
                n += 1
                yield n, pos

        times_to_move += 1


def get_sum_neighbors(d, pos):
	s = 0
	for n in [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]:
		idx = (pos[0]+n[0], pos[1]+n[1])
		s += d[idx]
	return s

# Part One
puzzle_input = 347991
sp = spiral(puzzle_input)
try:
	while True:
		n, pos = next(sp)
except StopIteration:
	pass

print(abs(pos[0]) + abs(pos[1]))

# Part Two
sp = spiral(puzzle_input)
s = defaultdict(lambda: 0)
s[(0,0)] = 1
next(sp)
while True:
	_, pos = next(sp)
	v = get_sum_neighbors(s, pos)
	if v > puzzle_input:
		print(v)
		break
	s[pos] = v
