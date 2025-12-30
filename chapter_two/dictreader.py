import csv


with open(file="try.csv", mode="r") as f:
    reader= csv.DictReader(f)
    for row in reader:
        print(row["Name"], ' ', row['Address'])