#dictwriter use gareko
import csv

data =[
    {"name":"Manav", "address": "Dharan", "age": 23},
    {"name":"msom", "address":"sodhu_parxa", "age": 20}
]
with open (file="newnew.csv", mode="w", newline="") as f:
    writer = csv.DictWriter(f)
    writer.writeheader()
    writer.writerows(data)


#############not working####################