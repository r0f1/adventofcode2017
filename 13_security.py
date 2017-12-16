from collections import defaultdict

def is_at_top_at_step(layerlen, step):
    if layerlen == 0: return False
    if step == 0:     return True
    if step % (2*layerlen-2) == 0: return True
    return False

d = defaultdict(lambda: 0)
depth = 0

with open("13_input.txt") as f:
    for line in f:
        chunks = line.split(":")
        d[int(chunks[0])] = int(chunks[1])
        depth = int(chunks[0])

res = 0
for pos in range(depth+1):
    if is_at_top_at_step(d[pos], pos):
        res += d[pos] * pos

print(res) # Part One

delay = 0
while True:
    for pos in range(depth+1):
        if is_at_top_at_step(d[pos], pos+delay):
            break
    else:
        print(delay) # Part Two
        break
    delay += 1
