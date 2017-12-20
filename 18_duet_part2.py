from collections import defaultdict
import queue
from queue import Queue as Queue
from threading import Thread as Worker

def program(instructions, from_queue, to_queue, pid):

    registers = defaultdict(lambda: 0)
    registers["p"] = pid
    pc = 0
    send_counter = 0

    while True:
        instr = instructions[pc]
        chunks = instr.split()
        c = chunks[0]
        try:               x = int(chunks[1])
        except ValueError: x = registers[chunks[1]]

        if c == "snd":
            to_queue.put(x)
            send_counter += 1
        elif c == "rcv":
            try:
                registers[chunks[1]] = from_queue.get(timeout=5)
            except queue.Empty:
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

    if pid == 1:
        print(send_counter)

if __name__ == "__main__":

    with open("18_input.txt") as f:
        instructions = [l.strip() for l in f.readlines()]

    q0 = Queue()
    q1 = Queue()
    p1 = Worker(target=program, args=(instructions, q0, q1, 0))
    p2 = Worker(target=program, args=(instructions, q1, q0, 1))

    p1.start()
    p2.start()
    p1.join()
    p2.join()