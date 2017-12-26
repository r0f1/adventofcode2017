from collections import Counter

def pairs(it):
    try:
        while True:
            yield "%s%s" % (next(it), next(it))
    except StopIteration:
        pass

def to_cols(p):
    if len(p) == 5:
        line1, line2 = p.split("/")
        return line1[0]+line2[0], line1[1]+line2[1]
    else:
        line1, line2, line3 = p.split("/")
        return line1[0]+line2[0]+line3[0], line1[1]+line2[1]+line3[1], line1[2]+line2[2]+line3[2]


def rotate_flip_pattern(p):
    res = []
    res.append(p.replace("/", ""))
    if len(p) == 5:
        line1, line2 = p.split("/")
        col1, col2 = to_cols(p)
        res.append("%s%s" % (line2, line1))
        res.append("%s%s" % (line1[::-1], line2[::-1]))
        res.append("%s%s" % (col1[::-1], col2[::-1]))
        res.append("%s%s" % (line2[::-1], line1[::-1]))
        res.append("%s%s" % (col2, col1))
    else:
        line1, line2, line3 = p.split("/")
        col1, col2, col3 = to_cols(p)
        res.append("%s%s%s" % (line3, line2, line1))
        res.append("%s%s%s" % (line1[::-1], line2[::-1], line3[::-1]))
        res.append("%s%s%s" % (col1[::-1], col2[::-1], col3[::-1]))
        res.append("%s%s%s" % (line3[::-1], line2[::-1], line1[::-1]))
        res.append("%s%s%s" % (col3, col2, col1))
    return res #set(res)

def transform(patterns, p):
    size = int(len(p.replace("/", "")) ** 0.5)
    if size == 3:
        return patterns[p]

    #   transformed = []
    #   if size % 2 == 0:
    #       lines = iter(p.split("/"))
    #       for _ in range(size):
    #           chunks = []
    #           line1 = next(lines)
    #           chunks.append([a] for a in pairs(line1))
    #           line2 = next(lines)
    #           for i, a in pairs(line2):
    #               chunks[i] += "/" + a
    #           for c in chunks:
    #               transformed.append(patters[c])
    #       print(transformed)
    #       raise Exception()
    #   else:
    #       pass


patterns = {} 

with open("21_input.txt") as f:
    for line in f:
        p1, p2 = [p.strip() for p in line.split(" => ")]
        # if p1 == ".##/#.#/#..":
        #     print(rotate_flip_pattern(p1))
        for p in rotate_flip_pattern(p1):
            patterns[p] = p2

assert len(patterns) == (2**4 + 2**9)
print(len(patterns))

# p = ".#...####"
# for _ in range(5):
#     p = transform(patterns, p)

# print(Counter(p)["#"])
