from collections import Counter

def dfs(cur, graph, visited, too_heavy):
    if cur not in graph or cur in visited:
        return
    else:
        visited.add(cur)
        weights = [get_weight(n, graph) for n in graph[cur][1]]

        if weights:
            cnt = Counter(weights)
            # Balanced
            if len(cnt) == 1:
                return

            for k in cnt:
                if cnt[k] == 1:
                    iTarget = 0
                    for i, v in enumerate(weights):
                        if v == k:
                            iTarget = i
                            break
                    too_heavy.append(graph[cur][1][iTarget])
                    dfs(graph[cur][1][iTarget], graph, visited, too_heavy)

def get_weight(cur, graph):
    if cur not in graph:
        return 0
    else:
        total = sum([get_weight(n, graph) for n in graph[cur][1]])
        return graph[cur][0] + total

if __name__ == '__main__':
    with open('aoc7.txt', 'r') as f:
        graph = {}
        for line in f:
            a = line.split("->")
            if len(a) == 1:
                par, chl = a[0], ""
            else:
                par, chl = a
            parent, weight = par.split()
            weight = int(weight[1:len(weight) - 1])
            if chl:
                childs = list(map(lambda x: x.strip(), chl.strip().split(",")))
            else:
                childs = []
            graph[parent] = (weight, childs)

        cur = "vtzay" # From part 1
        too_heavy = []
        dfs(cur, graph, set(), too_heavy)
        for x in too_heavy:
            print('Too heavy: {}'.format(graph[x]))
