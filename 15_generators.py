def genA():
    x = 783
    while True:
        x *= 16807
        x %= 2147483647
        yield bin(x)[2:].zfill(16)[-16:]

def genB():
    x = 325
    while True:
        x *= 48271
        x %= 2147483647
        yield bin(x)[2:].zfill(16)[-16:]

def genA2():
    x = 783
    while True:
        x *= 16807
        x %= 2147483647
        if x % 4 == 0:
            yield bin(x)[2:].zfill(16)[-16:]    

def genB2():
    x = 325
    while True:
        x *= 48271
        x %= 2147483647
        if x % 8 == 0:
            yield bin(x)[2:].zfill(16)[-16:]

def judge(a, b, niter):
    res = 0
    for i in range(niter):
        x = next(a)
        y = next(b)
        if x == y:
            res += 1
    return res

print(judge(iter(genA()), iter(genB()), 40_000_000)) # Part One
print(judge(iter(genA2()), iter(genB2()), 5_000_000)) # Part Two

