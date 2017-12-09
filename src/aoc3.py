def solve(n):
    N = 100
    m = [[0]*N for i in range(N)]
    r = N // 2
    c = N // 2
    m[r][c] = 1
    while True:
        for i in range(1, N//2):
            while abs(c+1 - N//2) <= i:
                c += 1
                m[r][c] = sum_adj(m,r,c)
                if m[r][c] > n:
                    return m[r][c]
            while abs(r-1 - N//2) <= i:
                r -= 1
                m[r][c] = sum_adj(m,r,c)
                if m[r][c] > n:
                    return m[r][c]
            while abs (c-1 - N//2) <= i:
                c -= 1
                m[r][c] = sum_adj(m,r,c)
                if m[r][c] > n:
                    return m[r][c]
            while abs(r+1 - N//2) <= i:
                r += 1
                m[r][c] = sum_adj(m,r,c)
                if m[r][c] > n:
                    return m[r][c]

def sum_adj(m,r,c):
    dx = [(-1,0), (0,-1), (0,1), (1,0), (-1,-1), (1,1), (-1,1), (1,-1)]
    coords = [(r + d[0], c + d[1]) for d in dx]
    coords = filter(lambda d: d[0] >= 0 and d[1] >= 0 and d[0] < len(m) and d[1] < len(m[0]),
        coords)
    return sum([m[row][col] for row, col in coords])

def sum_adj_alt(m,r,c):
    ans = 0
    dx = [(-1,0), (0,-1), (0,1), (1,0), (-1,-1), (1,1), (-1,1), (1,-1)]
    for d in dx:
        rr = r + d[0]
        cc = c + d[1]
        if rr >= 0 and cc >= 0 and rr < len(m) and cc < len(m[0]):
            ans += m[rr][cc]
    return ans

solve(4) == 5
solve(25) == 26
solve(747) == 806
