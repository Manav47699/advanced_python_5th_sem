import json 
with open(file="data.json", mode="r") as f:
    data = json.load(f)

print(data)

##############not working

data = {
    "name": "Manv", 
    "age": 20,
    "skills": ["Python", "Ml"]
}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)