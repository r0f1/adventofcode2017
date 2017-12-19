puzzle_input = 386

l = [0]
pos = 1
for i in range(1, 2018):
	l.insert(pos, i)
	pos = (pos + puzzle_input + 1) % len(l)

print(l[l.index(2017)+1])

##50000000