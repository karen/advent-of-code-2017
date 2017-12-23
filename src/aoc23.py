regs = {}
insts = open('aoc23.txt', 'r').read().splitlines()

def tryget(val):
    if val in regs:
        return regs[val]
    elif val.isalpha():
        return 0
    else:
        return int(val)
i = 0
cnt = 0
while i >= 0 and i < len(insts):
    inst = insts[i]
    op,x,y = inst.split()
    if x.isalpha() and x not in regs:
        regs[x] = 0
    if op == 'set':
        regs[x] = tryget(y)
    elif op == "sub":
        regs[x] -= tryget(y)
    elif op == "mul":
        cnt += 1
        regs[x] *= tryget(y)
    elif op == "jnz" and tryget(x) != 0:
        i += tryget(y) - 1
    i += 1
print('#`mul` ops:', cnt)

import math
b = 108100
c = 125100
cnt = 0
for num in range(b, c + 1, 17):
    sb = int(math.sqrt(num)) + 1
    prime = True
    for d in range(2, sb):
        if (num % d) == 0:
            prime = False
            break
    if not prime:
        cnt += 1
print('#Composite numbers:', cnt)
