from collections import defaultdict
from math import sqrt; 
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def run_program(registers, instructions):
    pc = 0
    mul_count = 0

    while 0 <= pc < len(instructions):
        instr = instructions[pc]
        chunks = instr.split()
        c = chunks[0]
        try:               x = int(chunks[1])
        except ValueError: x = registers[chunks[1]]
        try:               y = int(chunks[2])
        except ValueError: y = registers[chunks[2]]

        if c == "set":
            registers[chunks[1]] = y
        elif c == "sub":
            registers[chunks[1]] -= y
        elif c == "mul":
            registers[chunks[1]] *= y
            mul_count += 1
        elif c == "jnz" and x != 0:
            pc += y - 1
        pc += 1

    return mul_count
   
with open("23_input.txt") as f:
    instructions = [l.strip() for l in f]

registers = defaultdict(lambda: 0)
print(run_program(registers, instructions)) # Part One

# Part Two
# Program counts the number of not prime numbers between b and b+17000+1
h = 0
b = 67*100+100000
for i in range(b, b + 17000 + 1, 17):
    if not is_prime(i):
        h += 1
print(h)