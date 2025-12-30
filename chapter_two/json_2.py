import json
data = {
    "name": "Manv", 
    "age": 20,
    "skills": ["Python", "Ml"]
}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)


##############not working###############

#read a excel file, process the data and write the results to a new excel file, 60 bhnda badi marks aako fucheee haru pass aru fail

#pymongo