import json
import hashlib


with open("users.json", "r", encoding='utf-8') as myFile:
    datosUser = json.load(myFile)
try:
    nuevoDocument = open("secure-users.json", "w", encoding='utf-8')
except:
    open("secure-users.json", "x")
    nuevoDocument = open("secure-users.json", "w", encoding='utf-8')

listaUsers = []
for data in datosUser:
    newUser = data
    newUser["password"] = hashlib.sha224(newUser["password"].encode()).hexdigest()
    listaUsers.append(newUser)

json.dump(listaUsers, nuevoDocument, indent=1, ensure_ascii=False)
print(nuevoDocument)
