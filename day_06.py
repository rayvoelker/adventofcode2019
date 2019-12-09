# input = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L""".split("\n")

filename = 'day_06_input.txt'
input = open(filename).read().split("\n")

orbits = []
for line in input:
    orbit = line.split(")")
    orbits.append(orbit)

distinct_objects = set()
parents = {}
for o in orbits:
    parents[o[1]] = o[0]
    distinct_objects.add(o[0])
    distinct_objects.add(o[1])

orbs = {}
def get_num_orbits(p):
    if p not in orbs:
        if p in parents:
            orbs[p] = 1 + get_num_orbits(parents[p])
        else:
            orbs[p] = 0
    return orbs[p]

total = 0
while distinct_objects:
    current_object = distinct_objects.pop()
    total += get_num_orbits(current_object)

print(total)