import heapq

def mhdist(l):
    return sum(abs(e) for e in l)

def read_input():
    data = []
    with open("20_input.txt") as f:
        for line in f:
            c1, c2, c3 = line.split()
            ps, vs, aas = c1.split(","), c2.split(","), c3.split(",")
            p = [int(ps[0][3:]),  int(ps[1]),  int(ps[2][:-1])]
            v = [int(vs[0][3:]),  int(vs[1]),  int(vs[2][:-1])]
            a = [int(aas[0][3:]), int(aas[1]), int(aas[2][:-1])]
            data.append([p,v,a])
    return data


data = read_input()

for _ in range(1000):
    for p, v, a in data:
        v[0] += a[0]
        v[1] += a[1]
        v[2] += a[2]
        p[0] += v[0]
        p[1] += v[1]
        p[2] += v[2]

print(min((mhdist(p), idx) for idx, (p, v, a) in enumerate(data)))


destroyed = set()
data = read_input()
for _ in range(1000):
    for idx, (p, v, a) in enumerate(data):
        if idx not in destroyed:
            v[0] += a[0]
            v[1] += a[1]
            v[2] += a[2]
            p[0] += v[0]
            p[1] += v[1]
            p[2] += v[2]

    d = {}
    for idx, (p, _, _) in enumerate(data):
        if idx not in destroyed:
            t = tuple(p)
            if t in d:
                destroyed.add(idx)
                destroyed.add(d[t])
            else:
                d[t] = idx

print(len(data) - len(destroyed))