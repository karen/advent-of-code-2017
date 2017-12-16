import string
ops = []
with open('aoc16.txt', 'r') as f:
    ops = f.read().split(",")

# There are a large number of operations for part 2.
# The trick is to realise that the programs will eventually cycle.
# Thus, we can find the state at the end of the 1 billionth cycle
# by saving previous permutations.
def dance(rounds, progs):
    seen = []
    for i in range(rounds):
        if ''.join(progs) in seen:
            return (seen[rounds % len(seen)])
        else:
            seen.append(''.join(progs))
        for op in ops:
            if op[0] == 's':
                i = int(op[1:])
                progs = progs[n - i:] + progs[:n - i]
            elif op[0] == 'x':
                i1, i2 = map(int, op[1:].split("/"))
                progs[i1], progs[i2] = progs[i2], progs[i1]
            elif op[0] == 'p':
                c1, c2 = op[1:].split("/")
                i1, i2 = progs.index(c1), progs.index(c2)
                progs[i1], progs[i2] = progs[i2], progs[i1]
    return ''.join(progs)

n = 16
rounds = int(1e9)
progs = list(string.ascii_lowercase)[:n]
print(dance(rounds, progs))
