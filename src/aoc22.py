grid = open('aoc22.txt').read().splitlines()
grid = [list(x) for x in grid]

nr = len(grid)
nc = len(grid[0])

row = nr // 2
col = nc // 2

CLEAN, WEAKENED, INFECTED, FLAGGED = 0, 1, 2, 3

nodes = {(r,c): CLEAN if grid[r][c] == '.' else INFECTED for r in range(nr) for c in range(nc)}

LEFT, UP, DOWN, RIGHT = 0, 1, 2, 3

def turn(pos, state):
    r, c, d = pos
    nd = next_dir(d, state)
    if nd == RIGHT:
        c += 1
    elif nd == LEFT:
        c -= 1
    elif nd == DOWN:
        r += 1
    elif nd == UP:
        r -= 1
    return (r, c, nd)

def next_dir(cur, state):
    r = {RIGHT: DOWN, DOWN: LEFT, LEFT: UP, UP: RIGHT}
    l = {RIGHT: UP, DOWN: RIGHT, LEFT: DOWN, UP: LEFT}
    if state == CLEAN:
        return l[cur]
    elif state == INFECTED:
        return r[cur]
    elif state == WEAKENED:
        return cur
    elif state == FLAGGED:
        return 3 - cur # switch to opposite direction

cnt = 0
pos = (row, col, UP)
for i in range(10000000):
    row, col, _ = pos
    coord = (row, col)
    if coord in nodes and nodes[coord] != CLEAN:
        pos = turn(pos, nodes[coord])
        nodes[coord] += 1
        nodes[coord] %= 4
        if nodes[coord] == INFECTED:
            cnt += 1
    else:
        pos = turn(pos, CLEAN)
        nodes[coord] = 1
print(cnt)




