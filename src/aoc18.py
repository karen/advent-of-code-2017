def solve():
    insts = [[], []]
    with open('aoc18.txt', 'r') as f:
        insts[0] = [line for line in f]
    insts[1] = insts[0].copy()
    
    regs = [{'p': 0}, {'p': 1}]
    
    p = 1 # current program
    q = [[], []] # queue of values
    d = [False, False] # deadlock/wait indicators
    pc = [0, 0] # program counter

    cnt = 0

    # while there isn't a deadlock and we haven't jumped out of the program
    while (not d[0] or not d[1]) and pc[1-p] >= 0 and pc[1-p] < len(insts[0]):
        p = 1 - p
        i = pc[p] # current instruction for the current program
        split = insts[p][i].split()
        rg = ''
        if len(split) == 2:
            op, val = split
            if op == "snd":
                val_to_send = regs[p][val] if val in regs[p] else int(val)
                q[1-p].insert(0, val_to_send) # send value to the other program
                d[1-p] = False # allow other program to proceed
                if p == 1:
                    cnt += 1
            elif op == "rcv":
                if q[p]:
                    regs[p][val] = q[p].pop()
                elif not q[p]:
                    pc[p] -= 1 # don't advance to the next instruction
                    d[p] = True # wait for other program to send a value
        else:
            op, rg, val = split
            if not rg.isdigit() and rg not in regs[p]:
                regs[p][rg] = 0
            val = regs[p][val] if val in regs[p] else int(val)

            if op == "set":
                regs[p][rg] = val
            elif op == "add":
                regs[p][rg] += val
            elif op == "mul":
                regs[p][rg] *= val
            elif op == "mod":
                regs[p][rg] %= val
            elif op == "jgz" and (rg in regs[p] and regs[p][rg] > 0) or (rg not in regs[p] and int(rg) > 0):
                pc[p] += val - 1
        pc[p] += 1

    return cnt

print(solve())
