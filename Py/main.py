import tokenizer
import tokenParser

tokens = tokenizer.Tokenizer().tokenize("..\\External_Files\\main.txt")

print(tokenParser.Parser().parse(tokens, '..\\External_Files\\Grammar.txt', '..\\External_Files\\Reductions.txt'))
