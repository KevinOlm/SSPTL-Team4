import re

"definición de funciones"

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

#Función que verifica si un caracter es un operador relacional
def isOpRel(char):
    if (char == "<" or
        char == ">" or
        char == "=" or
        char == "!" or
        char == "&" or
        char == "|"):
        return True
    else:
        return False

#Función que devuelve el token de un operador relacional
def opRelToken(word):
    if(word == "<" or word == ">" or word == "<=" or word == ">="): return 7
    elif(word == "==" or word == "!="): return 11
    elif(word == "="): return 18
    elif(word == "!"): return 10
    elif(word == "&&"): return 9
    elif(word == "||"): return 8
    return False

#Función para crear tokens
def tokenCreator(name, value):
    token = { "word": name, "token": value }
    return token





"Programa principal"

#Abre el archivo y lo guarda como cadena de texto en la variable file_text
with open("C:\\Users\\Kevin Olmeda\\Desktop\\SSPTL - Team 4\\External_Files\\main.txt", "r") as file:
    file_text = file.read()

word = "" #variable que guarda las palabras reservadas e identificadores
oprel = "" #variable que guarda los operadores relacionales
tokens = [] #Arreglo que contendrá todos los valores de los tokens
string_ver = False #Variable que verifica si los caracteres se encuentran dentro de una cadena

#Recorre la variable file_text caracter por caracter
for char in file_text:
    #Si los valores se encuentran dentro de comillas, los agrega a una cadena
    if(string_ver):
        if(char == "\""): string_type = 3
        elif(char == "\n"): string_type = "Error: Cadena de caracteres no ha sido cerrada"
        else:
            word += char
            continue
        tokens.append(tokenCreator(word, string_type))
        word = ""
        string_ver = False
        continue
    #Verifica si existe una comilla que inicie 
    elif(char == "\""):
        string_ver = True
        if(len(word) <= 0): continue
    
    #Verifica si el caracter es alfanumérico, en caso de que sí, lo guarda en la variable word
    if(char.isalnum() or char == "."):
        word += char
        continue
    #En caso contrario, valida la palabra
    elif(len(word) > 0):
        if(re.fullmatch("[0-9]+", word)): word_type = 1
        elif(re.fullmatch("\d*\.{1}\d+", word)): word_type = 2
        elif(re.fullmatch("[a-zA-Z]\w*", word)):
            word_type = isReserved(word)
            if (not word_type): word_type = 0
        else: word_type = "Error, palabra no reconocida"
        tokens.append(tokenCreator(word, word_type))
        word = ""

    #Verifica si el caracter es una palabra reservada, en caso de que sí, lo guarda en la variable oprel
    if(isOpRel(char)):
        oprel += char
        continue
    #En caso contrario, valida el operador
    elif(len(oprel) > 0):
        oprel_type = opRelToken(oprel)
        if (not oprel_type): oprel_type = "Error, operador relacional no reconocido"
        tokens.append(tokenCreator(oprel, oprel_type))
        oprel = ""

    token_type = isSpChar(char) #Variable que guarda el tipo de token de los caracteres especiales
    #Verifica si el caracter es un caracter especial
    if(token_type):
        tokens.append(tokenCreator(char, token_type))
    #En caso de que sea un caracter extraño, marca error
    elif(char != "\t" and char != "\n" and char != " "):
        tokens.append(tokenCreator(char, "Error, caracter no reconocido"))

for tk in tokens:
    print(str(tk["word"]) + " es un token de tipo: " + str(tk["token"]))
