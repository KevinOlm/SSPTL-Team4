class Parser:

    def __init__(self):
        pass

    def __errorVerifier(self, tokens):
        for token in tokens:
            if(type(token['token']) is str):
                return False
        return True

    def __readTable(self, url):
        with open (url, 'r') as readedTable:
            writenTable = []
            for readedRow in readedTable:
                readedRow = readedRow.rstrip()
                writenRow = readedRow.split('\t')
                writenTable.append(writenRow)
        return writenTable

    def parse(self, tokens, grammarURL, reductionsURL):
        grammar = self.__readTable(grammarURL)
        reductions = self.__readTable(reductionsURL)
        
        if(not self.__errorVerifier(tokens)):
            return 'Existe un error léxico'

        parserPile = [23, 0]
        tokenCounter = 0
        finalToken = len(tokens)
        while(tokenCounter < finalToken):
            result = grammar[parserPile[-1]][tokens[tokenCounter]['token']]
            if(result == ''):
                return 'Existe un error sintáctico'
            elif(result.startswith('d')):
                parserPile.append(tokens[tokenCounter]['token'])
                parserPile.append(int(result[1:]))
                print(parserPile)
                tokenCounter += 1
            elif(result.startswith('r')):
                if(result == 'r0'):
                    return 'Programa Aceptado'
                
                reductionRule = int(reductions[int(result[1:])-1][0])
                reductionValue = int(reductions[int(result[1:])-1][1])
                if(reductionValue > 0):
                    del parserPile[len(parserPile)-(reductionValue)*2:]
                grammarValue = int(grammar[parserPile[-1]][reductionRule])
                parserPile.append(reductionRule)
                parserPile.append(grammarValue)
                print(parserPile)
