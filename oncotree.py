#Edit so that only single parent needs to be inputted

#rishab827



import json
oncotree = open("oncotree.json")
data = json.load(oncotree)

def write_json(data, filename="oncotree.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def search_field_recursive(data, field_name, parents=[]):
    results = []

    for key, value in data.items():
        if key == field_name:
            results.append(parents + [key])
        elif isinstance(value, dict):
            results.extend(search_field_recursive(value, field_name, parents + [key]))

    return results

with open("oncotree.json") as json_file:
    data = json.load(json_file)
    numLevel = int(input("What level is the parent function?  "))

valid_input = False
while not valid_input:
        getCode = input("Enter parent code: ")
        parents = []
        parents = search_field_recursive(data, getCode, parents)
        if not parents:
                print(f"Parent code '{getCode}' not found in the data. Input again: ")
        else:
                valid_input = True


if numLevel == 1:
        temp = data["TISSUE"]["children"][parents[0][2]]["children"]

elif numLevel == 2:
        temp = data["TISSUE"]["children"][parents[0][2]]["children"][parents[0][4]]["children"]

elif numLevel == 3:
        temp = data["TISSUE"]["children"][parents[0][2]]["children"][parents[0][4]]["children"][parents[0][6]]["children"]

elif numLevel == 4:
        temp = data["TISSUE"]["children"][parents[0][2]]["children"][parents[0][4]]["children"][parents[0][6]]["children"][parents[0][8]]["children"]

elif numLevel == 5:
        temp = data["TISSUE"]["children"][parents[0][2]]["children"][parents[0][4]]["children"][parents[0][6]]["children"][parents[0][8]]["children"][parents[0][10]]["children"]

elif numLevel == 6:
        temp = data["TISSUE"]["children"][parents[0][2]]["children"][parents[0][4]]["children"][parents[0][6]]["children"][parents[0][8]]["children"][parents[0][10]]["children"][parents[0][12]]["children"]


exists = False
while not exists:
        newCode = input("Enter code of new code: ")
        if search_field_recursive(data, newCode):
                print("Error: New code already exists. Try again: ")
        else:
                exists = True

newColor = input("Enter color of new color: ")
newName = input("Enter name of new name: ")
newMainType = input("Enter name of new mainType: ")
newTissue = input("Enter name of new tissue: ")
newParent = input("Enter name of new parent: ")


temp.update({ newCode: {
                                "code": newCode,
                                "color": newColor,
                                "name": newName,
                                "mainType": newMainType,
                                "externalReferences": {},
                                "tissue": newTissue,
                                "children": {},
                                "parent": newParent,
                                "history": [],
                                "level": int(numLevel) + 1,
                                "revocations": [],
                                "precursors": []
                            }})


if numLevel == 1:
        data["TISSUE"]["children"][parents[0][2]]["children"] = temp

elif numLevel == 2:
        data["TISSUE"]["children"][parents[0][2]]["children"][parents[0][4]]["children"] = temp

elif numLevel == 3:
        data["TISSUE"]["children"][parents[0][2]]["children"][parents[0][4]]["children"][parents[0][6]]["children"] = temp

elif numLevel == 4:
        data["TISSUE"]["children"][parents[0][2]]["children"][parents[0][4]]["children"][parents[0][6]]["children"][parents[0][8]]["children"] = temp

elif numLevel == 5:
        data["TISSUE"]["children"][parents[0][2]]["children"][parents[0][4]]["children"][parents[0][6]]["children"][parents[0][8]]["children"][parents[0][10]]["children"] = temp

elif numLevel == 6:
        data["TISSUE"]["children"][parents[0][2]]["children"][parents[0][4]]["children"][parents[0][6]]["children"][parents[0][8]]["children"][parents[0][10]]["children"][parents[0][12]]["children"] = temp

write_json(data)
