import json

with open('D:\\ORG_REPO\\MR-Automation-Project\\api-test-python-request\\jsonfiletest.json') as file:
    jsonData = json.load(file)

#loop skill, then parse value of "level" if the name is "ngoding" --> "expert"
for course in jsonData['data']['skill']:
    if course['name'] == "ngoding":
        print(course['level'])
        print('==========================================')

for course in jsonData['data']['skill']:
    print(course['level'])