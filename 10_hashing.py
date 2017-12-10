from functools import reduce
import operator

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

def hashing(length_sequence, m, curr, skip):
    for p in length_sequence:
        n = reversed_part(m, curr, p)
        alter_list(m, n, curr)
        curr = (curr + p + skip) % len(m)
        skip = (skip + 1) % len(m)
    return curr, skip

length_sequence = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]
m = list(range(256))
curr = 0
skip = 0
hashing(length_sequence, m, curr, skip)
print(m[0]*m[1]) # Part One


puzzle_input_str = ",".join(str(p) for p in length_sequence)
sequence = [ord(p) for p in puzzle_input_str] + [17,31,73,47,23]
m = list(range(256))
curr = 0
skip = 0
for _ in range(64):
    curr, skip = hashing(sequence, m, curr, skip)

sparse_hash = [reduce(operator.xor, m[i*16:(i+1)*16]) for i in range(16)]
dense_hash = ["{0:02x}".format(x) for x in sparse_hash]
print("".join(dense_hash)) # Part Two