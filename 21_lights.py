def rotate_flip_pattern(p):
	res = []
	if len(p) == 4:
		line1, line2 = p.split("/")
		res.append("%s/%s" % (line1, line2))
		res.append("%s/%s" % (line2, line1))

	else:
		pass

patterns = {}

with open("21_input.txt") as f:
	for line in f:
		p1, p2 = [p.strip() for p in line.split(" => ")]
