def func(alist, part):
	n = list(alist)
	steps = 0
	i = 0
	try:
		while True:
			p = n[i]
			if part == 2 and n[i] >= 3: n[i] -= 1
			else:                       n[i] += 1
			i += p
			steps += 1
	except IndexError:
		pass
	print(steps)

with open("05_input.txt", "r") as f:
	n = [int(x) for x in f.read().splitlines()]

func(n, part=1) # Part One
func(n, part=2) # Part Two
