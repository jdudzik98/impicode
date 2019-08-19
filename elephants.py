import sys

"""Input mechanism"""

data = []

lines = sys.stdin.readlines()

for single_line in lines:
    single_line = single_line.replace('\n', '').split(" ")
    data.append(single_line)

"""Turning data into permutation list"""
data[4] = []

for elephants in range(1, int(data[0][0]) + 1):

    data[4].append(data[2][int(data[3].index(str(elephants)))])
del data[2], data[3]