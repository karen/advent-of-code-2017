def generate(cur, data):
        fsm = {'a': [(1, 1, 'b'), (0, -1, 'c')],
               'b': [(1, -1, 'a'), (1, 1, 'd')],
               'c': [(1, 1, 'a'), (0, -1, 'e')],
               'd': [(1, 1, 'a'), (0, 1, 'b')],
               'e': [(1, -1, 'f'), (1, -1, 'c')],
               'f': [(1, 1, 'd'), (1, 1, 'a')]}
        state, pos = cur
        val, dx, nstate = fsm[state][data.get(pos, 0)]
        data[pos] = val
        return (nstate, pos + dx)

steps = 12919244
cur = ('a', 0)
data = {}
for i in range(steps):
    cur = generate(cur, data)
print(sum(data.values()))
