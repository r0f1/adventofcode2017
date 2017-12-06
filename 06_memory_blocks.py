import itertools

puzzle_input = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"
mem = [int(i) for i in puzzle_input.split()]
configs = dict()
configs[str(mem)] = 0
count = 0
while True:
	maxidx, v = max(enumerate(mem), key=lambda p: p[1])
	mem[maxidx] = 0
	k = list(range(len(mem)))
	idxs = itertools.cycle(k[maxidx+1:]+k[:maxidx+1])
	while v > 0:
		i = next(idxs)
		mem[i] += 1
		v -= 1
	count += 1
	c = str(mem)
	if c in configs:
		break
	configs[c] = count
print(count)            # Part One
print(count-configs[c]) # Part Two