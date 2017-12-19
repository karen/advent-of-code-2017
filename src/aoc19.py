grid = []
with open('aoc19.txt', 'r') as f:
    grid = f.read().splitlines()

r, c= 0, grid[0].index('|')

RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3

ans = '> '
cur = DOWN
steps = 0
# assumes that we only get well-formed graphs i.e. intersections formed by '+'
# |            |
# |            |
# |            |
# +   and not      which leads to "the end" of the graph
while grid[r][c] != ' ':
    steps += 1
    if grid[r][c].isalpha():
        ans += grid[r][c]
    # as long as it is valid, we move in that direction
    if cur == DOWN and r + 1 < len(grid):
        r += 1
    elif cur == UP and r - 1 >= 0:
        r -= 1
    elif cur == LEFT and c - 1 >= 0:
        c -=1
    elif cur == RIGHT and c + 1 < len(grid[r]):
        c += 1
    # key point is that the direction changes occur only at '+'
    if grid[r][c] == '+':
        if cur == DOWN or cur == UP:
            cur = LEFT if grid[r][c-1] != ' ' else RIGHT
        else:
            cur = DOWN if grid[r+1][c] != ' ' else UP   

print(ans)
print(steps)