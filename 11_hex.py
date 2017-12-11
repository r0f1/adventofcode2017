from collections import Counter
import functools

with open("11_input.txt") as f:
	moves = next(f).strip().split(",")

def calculate_steps(c):
	d = {}
	d["n"]  = c["n"]  - c["s"]
	d["nw"] = c["nw"] - c["se"]
	d["ne"] = c["ne"] - c["sw"]
	x = d["ne"] - d["nw"]
	y = 2*d["n"] + d["ne"] + d["nw"]
	return (abs(x)+abs(y)) // 2

c = Counter(moves)
print(calculate_steps(c)) # Part One

m = 0
c = Counter()
for e in moves:
	c[e] += 1
	m = max(m, calculate_steps(c))
print(m) # Part Two