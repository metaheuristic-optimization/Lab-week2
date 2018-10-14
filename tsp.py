#!/usr/bin/python
import sys

dataset = sys.argv[1]
datasetPath = './dataset/' + dataset

print('Reading dataset: ', datasetPath)

lines = open(datasetPath).read().split("\n")

total = lines[0]

print("Total cities: ", total)

lines.pop(0)

cities = {}

for x in lines:
    line = x.split(' ')
    if len(line) == 3:
        print(line)
        cities[line[0]] = {
        'lat': line[1],
               'lng': line[2]
        }

print(cities)