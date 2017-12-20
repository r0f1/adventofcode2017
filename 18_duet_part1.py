from collections import defaultdict

with open("18_input.txt") as f:
    instructions = [l.strip() for l in f.readlines()]

registers = defaultdict(lambda: 0)
sound = None
recovered = None
pc = 0

while True:
    instr = instructions[pc]
    chunks = instr.split()
    c = chunks[0]
    try:               x = int(chunks[1])
    except ValueError: x = registers[chunks[1]]

    if c == "snd":
        sound = x
    elif c == "rcv":
        if x != 0:
            recovered = sound
            if recovered is not None:
                print(recovered)
                break
    else:
        try:               y = int(chunks[2])
        except ValueError: y = registers[chunks[2]]

        if c == "set":
            registers[chunks[1]] = y
        elif c == "add":
            registers[chunks[1]] += y
        elif c == "mul":
            registers[chunks[1]] *= y
        elif c == "mod":
            registers[chunks[1]] %= y
        elif c == "jgz" and x > 0:
            pc += y - 1
    pc += 1
