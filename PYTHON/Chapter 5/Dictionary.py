Aryan = {} # empty dictionaries 
Data = {
    "name" : "Aryan",
    "origin" : "Indian",
    "Phone No." : "9421066846",
    "marks" : [25, 56, 98]
}

# print(Data["name"])
# print(Data["marks"])

# print(Data.items()) => gives list of data 
# print(Data.keys())
Data.update({"Friend": "Myself"})
# print(Data)

print(Data.get("Friend"))
# print(Data["name"]) this will give error when key is not present while above method will gine "None" at same situation


