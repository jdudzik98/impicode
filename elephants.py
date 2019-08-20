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

    data[4].append(int(data[2].index(data[3][elephant-1])+1))

del data[3], data[2]