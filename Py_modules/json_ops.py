import json

dataDict = {
    "sampleString": "Great Automation Framework",
    "sampleList": ["Good", "Better", "Best"],
    "sampleTuple": ("Python", "Pytest", "Automation"),
    "sampleObj": {"platform": "Udemy", "Valuable": True},
    "sampleInteger": 555,
    "booleanValue": True,
    "noneValue": None
}

print("convert py dict to JSON string")
resultJSON = json.dumps(dataDict, sort_keys=True, indent=4)
# print(resultJSON)
print(type(resultJSON))
print(type(resultJSON) == str)

# {
#     "sampleString": "Great Automation Framework",
#     "sampleList": [
#         "Good",
#         "Better",
#         "Best"
#     ],
#     "sampleTuple": [
#         "Python",
#         "Pytest",
#         "Automation"
#     ],
#     "sampleObj": {
#         "platform": "Udemy",
#         "Valuable": true
#     },
#     "sampleInteger": 555,
#     "booleanValue": true,
#     "noneValue": null
# }

print("convert JSON string to py dict")
resultDict = json.loads(resultJSON)
print(resultDict)
print(type(resultDict))

print("convert JSON file to py dict")
with open('example.json', 'r') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data.keys())
    print(data.values())

    for k, v in data.items():
        print(k, ":", v)


def validateJSON(jsonstr):
    try:
        json.loads(jsonstr)
    except ValueError as err:
        return False
    return True


JsonString = """{"name": "Raji", "salary": 25000, "email": "raji@mymail.com",}"""
isValid = validateJSON(JsonString)
print("Json string passed is valid?", isValid)
