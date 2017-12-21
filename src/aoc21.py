import numpy as np

def to_matrix(s):
    assert(type(s) == str)
    return np.array([list(x) for x in s.split("/")])

def to_str(mat):
    str = ''
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            str += (mat[r][c])
        if r != len(mat) - 1:
            str += ("/")
    return str

def enhance(currMat):
    if len(currMat) % 2 == 0:
        return enhanceBy(2, currMat)
    else:
        return enhanceBy(3, currMat)

def enhanceBy(size, mat):
    submatrices = traverse(size, mat)
    k = len(mat) // size
    pieces = []
    for row in submatrices:
        pieces.append([])
        for entry in row:
            pieces[-1].append(match(strToTfm, entry))
    result = [np.hstack(row) for row in pieces]
    result = np.vstack(result)
    return result

def traverse(size, mat):
    result = []
    stride = size
    for r in range(len(mat) // size):
        row = []
        for c in range(len(mat) // size):
            entry = []
            for rr in range(size):
                for cc in range(size):
                    entry.append(mat[r*stride + rr][c*stride + cc])
            row.append(np.array(entry).reshape(size,size))
        result.append(row)
    return np.array(result)

def match(mp, matrix):
    return to_matrix(mp[to_str(matrix)])

def generate(mp, string, value):
    matrix = to_matrix(string)
    possibilities = []
    possibilities.extend(generateRotations(matrix))
    possibilities.extend(generateRotations(np.flip(matrix, 0)))
    possibilities.extend(generateRotations(np.flip(matrix, 1)))
    want = set(to_str(x) for x in possibilities)
    for key in want:
        mp[key] = value

def generateRotations(matrix):
    return [np.rot90(matrix, r) for r in range(4)]

strToTfm = {}
currKey = ".#./..#/###"
curr = to_matrix(currKey)

with open('aoc21.txt', 'r') as f:
    for line in f:
        before, after = line.split("=>")
        before, after = before.strip(), after.strip()
        generate(strToTfm, before, after)
for t in range(19):
    cnt = 0
    for r in range(len(curr)):
        for c in range(len(curr)):
            if curr[r][c] == '#':
                cnt += 1
    print(t, cnt)
    curr = enhance(curr)
