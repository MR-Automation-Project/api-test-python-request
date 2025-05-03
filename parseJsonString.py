import json

# tambahan kutip 1 ' ' , karena saat json.load() harus bentuk string, tidak boleh dict!
courses = '{"age":35,"language":["Python","Java"],"name":"Miftah Ramadhan"}'
#Loads method parse json string and it returns dict
dict_courses = json.loads(courses)
print(f'the type is {type(dict_courses)}')
print(dict_courses)

print(type(dict_courses['age']))
print(dict_courses["age"])

print(type(dict_courses['language']))
print(dict_courses["language"])
print(dict_courses['language'][1])
print(dict_courses['language'][0])

print(dict_courses['name'])

num = [1, 2]
for i in range(2):
    bahasa = dict_courses['language'][i]
    urutan = num[i]
    print(f'bahasa ke {urutan} adalah {bahasa}')