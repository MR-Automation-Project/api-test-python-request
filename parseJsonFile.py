import json

with open('D:\\ORG_REPO\\MR-Automation-Project\\api-test-python-request\\jsonfiletest.json') as file:
    jsonData = json.load(file)

print(jsonData)
print(type(jsonData))

#parse level pada index 1 dari array skill --> "expert"
print(jsonData['data']['skill'][1]['level'])

#print data is_correct = True
print(f'nilai iscorrect adalah {jsonData['data']['is_correct']}')

#print class : string kosong ""
print(f'value dari class adalah {jsonData['data']["class"]}')

#print section : null value json --> in python terms null is None
print(f'value dari class adalah {jsonData['data']["section"]}')

#print value dari point berupa number desimal.
print(f'value dari point adalah {jsonData['data']["dashboard"]["point"]}')
print(type(jsonData['data']["dashboard"]["point"]))

#print value dari age berupa number bilangan bulat/int.
print(f'value dari age adalah {jsonData['data']["age"]}')
print(type(jsonData['data']["age"]))
