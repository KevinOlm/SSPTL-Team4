import re

#Función que verifica si un caracter es un caracter especial
def isSpChar(char):
    if (char == "+" or char == "-"): return 5
    elif (char == "*" or char == "/"): return 6
    elif (char == ";"): return 12
    elif (char == ","): return 13
    elif (char == "("): return 14
    elif (char == ")"): return 15
    elif (char == "{"): return 16
    elif (char == "}"): return 17
    elif (char == "="): return 18
    elif (char == "$"): return 23
    return False

#Función que verifica si la palabra es una palabra reservada
def isReserved(word):
    if (word == "int" or word == "float" or word == "void"): return 4
    elif (word == "if"):return 19
    elif (word == "while"): return 20
    elif (word == "return"): return 21
    elif (word == "else"): return 22
    return False

#Abre el archivo y lo guarda como cadena de texto en la variable file_text
with open("C:\\Users\\Kevin Olmeda\\Desktop\\SSPTL - Team 4\\External_Files\\main.txt", "r") as file:
    file_text = file.read()


word = "" #variable que guarda las palabras

#Recorre la variable file_text caracter por caracter
for char in file_text:
    token_type = isSpChar(char) #Variable que guarda el tipo de token de los caracteres especiales

    #Verifica si el caracter es alfanumérico, en caso de que sí, lo guarda en la variable word
    if(char.isalnum() or char =="_"):
        word += char
        continue
    #En caso contrario, valida la palabra
    elif(len(word) > 0):
        if (isReserved(word)):
            print(word + " es una palabra reservada")
        else:
            print(word + " Es una variable")
        word = ""
    #Verifica si el caracter es un caracter especial
    if(token_type):
        print("El caracter \"" + char + "\" es un token de tipo " + str(token_type))
