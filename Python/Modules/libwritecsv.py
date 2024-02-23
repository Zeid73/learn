import csv

header = ["Name", "Age"]
data = [["a", 23], ["b", 25]]

with open("NA.csv", "w", newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(data)
