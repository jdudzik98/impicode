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

    data[4].append(data[2].index(data[3][elephant-1]) + 1)

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
            x = data[2][int(x)-1]