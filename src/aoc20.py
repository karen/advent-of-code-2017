import re
from collections import defaultdict

pat = "p=\<(-?\d+,-?\d+,-?\d+)\>, v=\<(-?\d+,-?\d+,-?\d+)\>, a=\<(-?\d+,-?\d+,-?\d+)\>"
particles = []
with open('aoc20.txt', 'r') as f:
    for line in f:
        m = re.search(pat, line)
        particle = {}
        particle['p'] = list(map(int, m.group(1).split(",")))
        particle['v'] = list(map(int, m.group(2).split(",")))
        particle['a'] = list(map(int, m.group(3).split(",")))
        particles.append(particle)

def update(p):
    for i in range(3):
        p['v'][i] += p['a'][i]
    for i in range(3):
        p['p'][i] += p['v'][i]

def dist(p):
    return sum(map(abs, p['p']))

glb_particle = -1

while True:
    # part 1
    loc_dist = dist(particles[0])
    for i, p in enumerate(particles):
        update(p)
        d = dist(p)
        if d < loc_dist:
            loc_dist = d
            glb_particle = i
    # print(glb_particle)
    # part 2
    grouped = defaultdict(list)
    for i, p in enumerate(particles):
        key = tuple(p['p'])
        grouped[key].append(i)
    keep_idxs = filter(lambda x: len(x) == 1, grouped.values())
    keep_idxs = map(lambda sublist: sublist[0], keep_idxs)
    particles = list(map(lambda i: particles[i], keep_idxs))
    print(len(particles))
