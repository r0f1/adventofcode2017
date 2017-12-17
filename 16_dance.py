with open("16_input.txt") as f:
    moves = next(f).split(",")

alpha = "abcdefghijklmnop"

def dance(moves, niters):
    p = list(range(len(alpha)))
    seen = dict()
    first_rep = None
    for its in range(niters):
        for m in moves:
            if m.startswith("s"):
                n = int(m[1:])
                p = p[-n:]+p[:-n]
            else:
                a, b = m[1:].split("/")
                if m.startswith("x"):
                    a, b = int(a), int(b)
                elif m.startswith("p"):
                    a, b = p.index(alpha.index(a)), p.index(alpha.index(b))
                p[a], p[b] = p[b], p[a]
        
        s = "".join(alpha[i] for i in p)
        if s in seen:
            first_rep = its
            break
        else:
            seen[s] = its

    if first_rep:
        return dance(moves, niters % first_rep)
    else:
        return p

print("".join(alpha[i] for i in dance(moves, 1)))             # Part One
print("".join(alpha[i] for i in dance(moves, 1_000_000_000))) # Part Two
