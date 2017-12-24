from collections import defaultdict
comps = open('aoc24.txt', 'r').read().splitlines()
comps = map(lambda x: tuple(map(int, x.split("/"))), comps)
graph = defaultdict(list)

# create the undirected graph of components
for p1, p2 in comps:
    graph[p1].append((p1,p2,p1+p2))
    if p1 != p2:
        graph[p2].append((p1,p2,p1+p2))

def solve():
    ans, max_length = 0, 0
    longest = []
    def dfs(g, comp, visited, acc, prev, l):
        nonlocal max_length, longest
        if comp in visited:
            if l > max_length:
                longest = [acc]
                max_length = l
            elif l == max_length:
                longest.append(acc)
            return acc
        else:
            # use the component
            visited.add(comp)
            p1, p2, total = comp
            best = acc
            # the next port to connect to is the side we haven't used yet
            nex = p1 if p1 != prev else p2
            for neighbour in g[nex]:
                best = max(best, dfs(g, neighbour, visited, acc + total, nex, l+1))
            visited.remove(comp)
            return best
    
    for component in graph[0]:
        ans = max(ans, dfs(graph, component, set(), 0, 0, 0))
    print('Overall strongest: {}\nLongest and strongest: {} (length {})'.format(ans, max(longest), max_length))

solve()
