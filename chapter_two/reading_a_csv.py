import csv


with open(file="try.csv", mode="r") as f:
    reader= csv.reader(f)
    for row in reader:
        print(row)