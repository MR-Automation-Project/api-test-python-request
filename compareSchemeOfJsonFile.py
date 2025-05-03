import json

with open('D:\\ORG_REPO\\MR-Automation-Project\\api-test-python-request\\jsonfiletest.json') as f1:
    jsonData1 = json.load(f1)
with open('D:\\ORG_REPO\\MR-Automation-Project\\api-test-python-request\\jsonfiletest2.json') as f2:
    jsonData2 = json.load(f2)

assert jsonData1 == jsonData2, f'data is not same!'
