def solve1(fw):
    dmg = 0
    for k in fw:
        if k % period(fw, k) == 0:
            dmg += k * fw[k]
    return dmg

def solve2(fw):
    wait = 0
    while True:
        found = True
        for k in fw:
            if (k + wait) % period(fw, k) == 0:
                found = False
                break
        if found:
            return wait
        else:
            wait += 1

def period(fw, k):
    return (fw[k] - 1) * 2

fw = {}
with open('aoc13.txt', 'r') as f:
        fw = dict([tuple(map(int, line.split(": "))) for line in f])

print(solve1(fw))
print(solve2(fw))
