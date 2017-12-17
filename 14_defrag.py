from functools import reduce
from itertools import product
import operator
import scipy.sparse

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

def new_hashing(inputstr):
    sequence = [ord(p) for p in inputstr] + [17,31,73,47,23]
    m = list(range(256))
    curr = 0
    skip = 0
    for _ in range(64):
        curr, skip = hashing(sequence, m, curr, skip)

    sparse_hash = [reduce(operator.xor, m[i*16:(i+1)*16]) for i in range(16)]
    dense_hash = ["{0:02x}".format(x) for x in sparse_hash]
    long_hash = [bin(int(c,16))[2:].zfill(4) for x in dense_hash for c in x]
    return "".join(str(x) for x in long_hash)

def get_neighbors(data, x, y, size):
    if data[y][x] == 0: return [size**2-1]

    res = []
    if y > 0: 
        if data[y-1][x] == 1: res.append(x+(y-1)*(size-1))
    if y < len(data)-1:
        if data[y+1][x] == 1: res.append(x+(y+1)*(size-1))
    if x > 0:
        if data[y][x-1] == 1: res.append(x-1+y*(size-1))
    if x < len(data)-1:
        if data[y][x+1] == 1: res.append(x+1+y*(size-1))
    return res

puzzle_input = "vbqugkhl"

data = []
res = 0
for i in range(128):
    h = new_hashing("%s-%d" % (puzzle_input, i))
    h2 = [int(c) for c in h]
    res += sum(h2)
    data.append(h2)

print(res) # Part One

size = 129

row = []
col = []

for i, (y, x) in enumerate(product(range(size-1), range(size-1))):
    ns = get_neighbors(data, x, y, size)
    for n in ns: 
        row.append(i)
        col.append(n)

mat = scipy.sparse.csr_matrix(([1]*len(row), (row, col)), shape=(size**2, size**2))
n_components, labels = scipy.sparse.csgraph.connected_components(mat, directed=False)
print(max(labels[:128**2])) # Part Two
