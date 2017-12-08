from collections import defaultdict
import operator as op

regs = defaultdict(lambda: 0)
ops = {
	">":  op.gt,
	">=": op.ge,
	"==": op.eq,
	"!=": op.ne,
	"<=": op.le,
	"<":  op.lt
}

higest = 0
with open("08_input.txt") as f:
	for line in f:
		reg, inst, nr, _, reg2, rel, nr2 = line.split()
		if ops[rel](regs[reg2], int(nr2)):
			if inst == "inc":
				regs[reg] += int(nr)
				higest = max(higest, regs[reg])
			else:
				regs[reg] -= int(nr)

print(max(regs.values())) # Part One
print(higest)             # Part Two
