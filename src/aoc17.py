def solve1(step, n=2017):
    cur = 0
    state = [0]
    for val in range(1, n+1):
        cur = ((cur + step) % len(state)) + 1
        state.insert(cur, val)
    return state[state.index(n) + 1]

# This method works only because the index of the value we are interested in
# is small enough (i.e. 1)
def solve2(step, n=int(50e6)):
    cur, length = 0, 1
    ans = -1
    for val in range(1, n+1):
        cur = ((cur + step) % length) + 1
        if cur == 1:
            ans = val
        length += 1
    return ans

print(solve1(316))
print(solve2(316))
