def hexmove(cur, d):
    if d == 'n':
        return cur[0], cur[1] - 1
    elif d == 'ne':
        return cur[0] - 1, cur[1] - 1
    elif d == 'nw':
        return cur[0] + 1, cur[1]
    elif d == 's':
        return cur[0], cur[1] + 1
    elif d == 'se':
        return cur[0] - 1, cur[1]
    elif d == 'sw':
        return cur[0] + 1, cur[1] + 1

def solve(dirs):
    cur = (0, 0)
    furthest = 0
    for d in dirs:
        cur = hexmove(cur, d)
        furthest = max(furthest, max(abs(cur[0]), abs(cur[1])))
    print(cur)
    print(furthest)

if __name__ == '__main__':
    dirs = []
    with open('aoc11.txt', 'r') as f:
        for line in f:
            dirs = line.split(",")
    solve(dirs)
