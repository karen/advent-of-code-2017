def solve1(graph):
    gp = set()
    visited = set()
    dfs(graph, '0', visited, gp)
    return gp

def solve2(graph):
    cnt = 0
    visited = set()
    for k in graph:
        if k not in visited:
            cnt += 1
            dfs(graph, k, visited, set())
    return cnt

def dfs(g, n, visited, childs):
    if n in visited:
        return
    childs.add(n)
    visited.add(n)
    for c in g[n]:
        dfs(g, c, visited, childs)

if __name__ == '__main__':
    graph = {}
    with open('aoc12.txt', 'r') as f:
        for line in f:
            node, children = line.split('<->')
            node = node.strip()
            children = list(map(lambda x: x.strip(), children.split(",")))
            if node not in graph:
                graph[node] = []
            for c in children:
                if c not in graph[node]:
                    graph[node].append(c)
    print(len(solve1(graph)))
    print(solve2(graph))
