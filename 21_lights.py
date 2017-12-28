import numpy as np

def transform(pd, p):
    size = int(len(p)**0.5)
    if size in (2,3):
        return pd[p]
    
    if size % 2 == 0:
        s = 2
    else: 
        s = 3

    arr = np.array(p).reshape(size, size)
    lines = []
    for h in np.hsplit(arr, size // s):
        res = []
        for v in np.vsplit(h, size // s):
            t = transform(pd, tuple(v.flatten()))
            res.append(t)
        nd = int(len(t)**0.5)
        lines.append(np.concatenate(res, axis=0).reshape(len(res)*nd, nd))

    return tuple(np.concatenate(lines, axis=1).flatten())

class Pattern(object):
    def __init__(self, inpattern, outpattern):
        arr = np.array(self._convert(inpattern))
        if len(arr) == 4:
            arr = np.reshape(arr, (2,2))
        else:
            arr = np.reshape(arr, (3,3))
        self.patterns = [tuple(a.flatten()) for a in self._rotate_flip_pattern(arr)]
        self.outpattern = tuple(self._convert(outpattern))

    def _convert(self, p):
        return [1 if c == "#" else 0 for c in p.replace("/", "")]

    def _rotate(self, arr):
        return [np.rot90(arr, 1), np.rot90(arr, 2), np.rot90(arr, 3)]

    def _flip(self, arr):
        return [np.flipud(arr), np.fliplr(arr)]

    def _rotate_flip_pattern(self, p):
        p1, p2 = self._flip(p)
        return [p] + self._rotate(p) + [p1, p2] + self._rotate(p1) + self._rotate(p2)

pattern_dict = {} 

with open("21_input.txt") as f:
    for line in f:
        pat = Pattern(*[p.strip() for p in line.split(" => ")])
        for p in pat.patterns:
            pattern_dict[p] = pat.outpattern

assert len(pattern_dict) == (2**4 + 2**9)

p = (0,1,0,0,0,1,1,1,1)
for _ in range(5):
    p = transform(pattern_dict, p)
    # s = int(len(p)**0.5)
    # arr = np.array(p).reshape(s,s)
    # print(arr)

print(sum(p))

for _ in range(13):
    p = transform(pattern_dict, p)

print(sum(p))
