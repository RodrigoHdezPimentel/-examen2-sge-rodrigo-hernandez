import json
import pandas as pd
from datetime import datetime

with open("users.json", "r",  encoding='utf-8') as myFile:
    datosUser = json.load(myFile)


libraries = []
listaBooks = []
#Bucle para personas
for data in datosUser:
    #Bucle para libros
    for book in data["books"]:
        libro = {"bookId": book["bookId"], "bookTitle":book["bookTitle"], "bookEditorial": book["bookEditorial"],
                 "bookPublication": book["bookPublication"], "libraryId": book["libraryId"], "userId": data["userId"],
                 "userFullName": data["userName"] + " " + data["userSurname"]}
        listaBooks.append(libro)


libraries.append({"libraryId": listaBooks[0]["libraryId"], "books":[]})
for book in listaBooks:
    for i in range(0, len(libraries)):
        if book["libraryId"] == libraries[i]["libraryId"]:
            break
        elif i == len(libraries)-1:
            libraries.append({"libraryId": book["libraryId"], "books":[]})
            break

for book in listaBooks:
    for lib in libraries:
        if book["libraryId"] == lib["libraryId"]:
            lib["books"].append(book)


idLib = []
idBook = []
titulo = []
editorial = []
publicacion = []
idUser = []
nombreUser = []

for lib in libraries:
    for book in lib["books"]:
        idLib.append(lib["libraryId"])
        idBook.append(book["bookId"])
        titulo.append(book["bookTitle"])
        editorial.append(book["bookEditorial"])
        publicacion.append(book["bookPublication"])
        idUser.append(book["userId"])
        nombreUser.append(book["userFullName"])

        df = pd.DataFrame({'Id Biblioteca': idLib, 'Id Libro': idBook, "Titulo": titulo, "editorial": editorial,
                       "publicacion": publicacion, "idUser": idUser, "nombreUser": nombreUser})
        df.index.name = 'Registro'

documentoFinal = f"{datetime.now().strftime("%d")}-{datetime.now().strftime("%m")}-{datetime.now().strftime("%Y")}-libros-prestados.xlsx"
df.to_excel(documentoFinal)
