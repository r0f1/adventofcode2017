count = 0
count2 = 0
with open("04_input.txt", "r") as f:
	for l in f:
		chunks = l.split()
		r = len(chunks)
		if r == len(set(chunks)):
			count += 1
			s = set("".join(sorted(c)) for c in chunks)
			if r == len(s):
				count2 += 1
print(count)
print(count2)
