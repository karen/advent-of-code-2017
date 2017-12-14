from aoc10 import khash

def key_to_grid(key):
    grid = [key + '-' + str(i) for i in range(128)]
    grid = list(map(lambda x: khash(x)['part2'], grid))
    assert(len(x) == 32 for x in grid)
    
    res = []
    for i in range(len(grid)):
        res.append('')
        for c in grid[i]:
            res[-1] += bin(int(c, 16))[2:].zfill(4)
    assert(len(x) == 128 for x in res)
    # number of used squares
    cnt = sum(len(list(filter(lambda x: x == '1', rowhash))) for rowhash in res)
    
    region = 0
    def dfs(g,r,c,v):
        if r < 0 or c < 0 or r >= len(g) or c >= len(g[0]) or v[r][c] or g[r][c] != '1':
            return
        v[r][c] = True
        dfs(g, r-1, c, v)
        dfs(g, r+1, c, v)
        dfs(g, r, c-1, v)
        dfs(g, r, c+1, v)

    v = [[False]*128 for i in range(128)]
    for r in range(len(res)):
        for c in range(len(res[r])):
            if res[r][c] == '1' and not v[r][c]:
                region += 1
                dfs(res, r, c, v)
    return {'part1': cnt, 'part2': region}

print(key_to_grid('vbqugkhl'))
