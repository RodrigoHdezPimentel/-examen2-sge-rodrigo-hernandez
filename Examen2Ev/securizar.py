import json
import hashlib
import io


with io.open("users.json", "r", encoding="utf8") as myFile:
    datosUser = json.load(myFile)
try:
    nuevoDocument = io.open("secure-users.json", "w", encoding="utf8")
except:
    open("secure-users.json", "x")
    nuevoDocument = io.open("secure-users.json", "w", encoding="utf8")

listaUsers = []
for data in datosUser:
    newUser = data
    newUser["password"] = hashlib.sha224(newUser["password"].encode()).hexdigest()
    listaUsers.append(newUser)

json.dump(listaUsers, nuevoDocument, indent=1)
print(nuevoDocument)
