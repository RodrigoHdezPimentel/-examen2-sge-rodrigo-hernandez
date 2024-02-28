import pandas as pd
import json

try:
    with open("secure-users.json", "r", encoding='utf-8') as myFile:
        datosUser = json.load(myFile)


        ids = []
        nombres = []
        password = []

        for user in datosUser:
            ids.append(user["userId"])
            nombres.append(user["userName"])
            password.append(user["password"])

            df = pd.DataFrame({'Id Usuario': ids, 'Nombre': nombres, "password": password})
            df.index.name = 'Registro'

        documentoFinal = "usuarios.xlsx"
        df.to_excel(documentoFinal)
except:
    open("secure-users.json", "x", encoding='utf-8')
    print("Lo siento, archivo no encontrado, ejecute primero securizar.py")
