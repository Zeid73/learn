import csv

rows = list()
header = list()
with open("num.csv") as file:
    csvreader = csv.reader(file)
    header = next(file)
    for row in csvreader:
        rows.append(row)

print(header)
print(rows)
