import csv
import pprint

with open('YahooList.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]

print(l)

print(l[0][0])