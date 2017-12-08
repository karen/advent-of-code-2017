def cond(reg, r, op, val):
    val = int(val)
    if r not in reg:
        reg[r] = 0
    tests = {
    ">": lambda r, v: reg[r] > v,
    ">=": lambda r, v: reg[r] >= v,
    "<": lambda r, v: reg[r] < v,
    "<=": lambda r, v: reg[r] <= v,
    "==": lambda r, v: reg[r] == v,
    "!=": lambda r, v: reg[r] != v
    }
    return tests[op](r, val)

if __name__ == '__main__':
    reg = {}
    m = 0
    with open('aoc8.txt', 'r') as f:
        for line in f:
            r1, op, delta, _, r2, c_op, cmpv = line.strip().split()
            if (cond(reg, r2, c_op, cmpv)):
                delta = int(delta)
                sign = 1 if op == 'inc' else -1
                if r1 not in reg:
                    reg[r1] = 0
                reg[r1] += sign * delta
                m = max(m, reg[r1])
        print(max(reg.values()))
        print(m)
