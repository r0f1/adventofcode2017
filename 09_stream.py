with open("09_input.txt") as f:
	puzzle_input = next(f)

p_iter = iter(puzzle_input)
d = 0
result = 0
result2 = 0
ignore_mode = False
for c in p_iter:
	if c == "!": next(p_iter); continue
	if c == ">": ignore_mode = False; continue
	if ignore_mode:
		result2 += 1
	else:
		if   c == "<": ignore_mode = True
		elif c == "{": d += 1
		elif c == "}": result += d; d -= 1

print(result) # Part One
print(result2) # Part Two
