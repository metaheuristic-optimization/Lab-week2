#!/usr/bin/python

import sys

dataset = sys.argv[1]
datasetPath = './dataset/' + dataset

print('Reading dataset: ', datasetPath)

lines = open(datasetPath).read().split("\n")

total = lines[0]

print("Total cities: ", total)

lines.pop(0)

print(lines)