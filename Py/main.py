import tokenizer

tokens = tokenizer.Tokenizer().tokenize("..\\External_Files\\main.txt")

for token in tokens:
    print(token)
