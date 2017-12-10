def reversed_part(m, curr, p):
    end = p + curr
    if end >= len(m):
        n = m[curr:] + m[:end-len(m)]
    else:
        n = m[curr:end]    
    return reversed(n)

def alter_list(m, n, curr):
    for e in n:
        m[curr] = e
        curr = (curr + 1) % len(m)

puzzle_input = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]
m = list(range(256))
curr = 0
skip = 0

for p in puzzle_input:
    n = reversed_part(m, curr, p)
    alter_list(m, n, curr)
    curr = (curr + p + skip) % len(m)
    skip += 1

print(m[0]*m[1]) # Part One
