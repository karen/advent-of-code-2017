import re

def solve(arr):
    n = len(arr)
    k = n >> 1
    res = 0
    for i in range(n):
        jmp = (i + k) % n
        if arr[i] == arr[jmp]:
            res += arr[i]
    return res

if __name__ == '__main__':
    arr = []
    with open('aoc1.txt', 'r') as f:
        for line in f:
            for x in line:
                arr.append(x)
        print(solve(list(map(int, arr))))
