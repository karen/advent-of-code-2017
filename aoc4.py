def solve():
    with open('aoc4.txt', 'r') as f:
        return len(list(filter(lambda line: len(line.split()) == len(set(line.split())), f)))

def solve2():
    res = 0
    with open('aoc4.txt', 'r') as f:
        for line in f:
            sorted_data = list(map(lambda x: ''.join(sorted(x)), line.split()))
            if len(line.split()) == len(set(sorted_data)):
                res += 1
    return res

if __name__ == '__main__':
    print(solve())
    print(solve2())
