import sys

"""Input mechanism"""

data = []

lines = sys.stdin.readlines()

for single_line in lines:
    single_line = single_line.replace('\n', '').split(" ")
    data.append(single_line)

"""Turning data into permutation list"""

data.append([])

for elephant in range(1, int(data[0][0]) + 1):

    data[4].append(data[2][data[3].index(str(elephant))])

del data[3], data[2]

"""Turning permutation into single cycles"""

data.append([False]*int(data[0][0]))

cycles = []

c = 0

for i in range(len(data[3])):
    if not data[3][i]:
        c += 1
        x = i + 1
        while not data[3][x-1]:
            data[3][x-1] = True
            if len(cycles) != c:
                cycles.append([])
            cycles[int(c)-1].append(x)
            x = int(data[2][x-1])

"""Fetching cycles parameters"""

minimal_weight = 0
cycle_weights = []
cycle_mins = []

for weight in data[1]:
    minimal_weight = max(minimal_weight, int(weight))

maximal_weight = minimal_weight

for i in range(c):
    cycle_weights.append(0)
    cycle_mins.append(maximal_weight)

    for e in cycles[i]:
        cycle_weights[i] += int(data[1][e-1])

        if int(data[1][e-1]) < int(cycle_mins[i]):
            cycle_mins[i] = data[1][e-1]

    if int(cycle_mins[i]) < int(minimal_weight):
        minimal_weight = cycle_mins[i]

"""Calculating the output"""

w = 0

for i in range(c):
    method_1 = cycle_weights[i] + (len(cycles[i]) - 2)*int(cycle_mins[i])
    method_2 = cycle_weights[i] + int(cycle_mins[i]) + (len(cycles[i]) + 1)*int(minimal_weight)
    w += min(method_1, method_2)
print(w)