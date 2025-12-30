import csv

data =[
    ["Name", "Address", "Age"],
    ["Ram ", "Dharan", 22],
    ["Shyam"," Itahari", 23],
    ["Hari", "Biratnager", 21]

]

with open(file="new.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(data)