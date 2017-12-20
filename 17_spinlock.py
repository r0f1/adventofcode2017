puzzle_input = 386

l = [0]
pos = 1
for i in range(1, 2018):
	l.insert(pos, i)
	pos = (pos + puzzle_input + 1) % len(l)

print(l[l.index(2017)+1])

after_zero = 0
pos = 0
for i in range(1, 50_000_001):
	pos = ((pos + puzzle_input) % i) + 1
	if pos == 1:
		after_zero = i

print(after_zero)
