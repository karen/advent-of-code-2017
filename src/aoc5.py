def solve(jumps):
    cnt, cur = 0, 0
    while cur >= 0 and cur < len(jumps):
        cnt += 1
        prev = cur
        cur += jumps[cur]
        jumps[prev] += 1
    return cnt

def solve2(jumps):
    cnt, cur = 0, 0
    while cur >= 0 and cur < len(jumps):
        cnt += 1
        prev = cur
        cur += jumps[cur]
        if jumps[prev] >= 3:
            jumps[prev] -=1
        else:
            jumps[prev] += 1
    return cnt

if __name__ == '__main__':
    jumps = []
    with open('aoc5.txt', 'r') as f:
        jumps = list(map(int, f))
    print(solve(jumps))
    print(solve2(jumps))
