import csv

# open the csv file
file = open("file.csv")

# use the csv.reader objcet to read the csv file
csvreader = csv.reader(file)

# extract the field names
header = []
header = next(csvreader)

# extract the rows
rows = []
for row in csvreader:
    rows.append(row)

# close the file
file.close()

#################

import csv

# define a filename and open the file
filename = "file.csv"

# to avoid forgeten to close the file use with() statment
with open(filename, "w", newline="") as file:
    # create a csvwriter object
    csvwriter = csv.writer(file)

    # write the header (single line)
    csvwriter.writerow(header)

    # write the rest of the data (multi line)
    csvwriter.writerows(data)
