def solve(matrix):
    res = 0
    for r in range(len(matrix)):
        row = matrix[r]
        res += max(row) - min(row)
    return res

def solve2(matrix):
    res = 0
    for r in range(len(matrix)):
        for i in range(len(row)):
            for j in range(len(row)):
                if i == j:
                    continue
                if row[i] % row[j] == 0:
                    res += row[i] / row[j]
    return res

if __name__ == '__main__':
    matrix = []
    with open('aoc2.txt', 'r') as f:
        for line in f:
            matrix.append(list(map(int, line.strip().split('\t'))))
    print(solve2(matrix))
