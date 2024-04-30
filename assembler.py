from parser import Parser
from code import Code
from symbolTable import SymbolTable


class Assembler:

    def __init__(self, path):
        self.parser = Parser(path)
        self.code = Code()
        self.symbolTable = SymbolTable()
        self.translated = ""

    def firstIteration(self):
        counter = 0
        while self.parser.hasMoreCommands():
            self.parser.advance()
            cmdType = self.parser.commandType()
            if cmdType in ["A_COMMAND", "C_COMMAND"]:
                counter += 1
            elif cmdType == "L_COMMAND":
                self.symbolTable.addEntry(self.parser.symbol(), counter)
        self.parser.curIndex = -1

    def secondIteration(self):
        counter = 16
        while self.parser.hasMoreCommands():
            self.parser.advance()
            if self.parser.commandType() == "A_COMMAND":
                symbol = self.parser.symbol()

                # print(symbol, counter)
                if not self.symbolTable.contains(symbol) and not symbol.isnumeric():
                    self.symbolTable.addEntry(symbol, counter)
                    counter += 1
        self.parser.curIndex = -1

    def toBinary(self, num):
        return bin(int(num))[2:].zfill(16)

    def translate(self):
        while self.parser.hasMoreCommands():
            self.parser.advance()
            if self.parser.commandType() == "A_COMMAND":
                symbol = self.parser.symbol()
                if symbol.isnumeric():
                    self.translated += self.toBinary(symbol)
                else:
                    address = self.symbolTable.getAddress(symbol)
                    self.translated += self.toBinary(address)
                self.translated += '\n'

            elif self.parser.commandType() == "C_COMMAND":
                res = '111'
                dest = self.code.dest(self.parser.dest())
                comp = self.code.comp(self.parser.comp())
                jump = self.code.jump(self.parser.jump())

                res += comp + dest + jump + '\n'
                self.translated += res

        return self.translated

    def writeFile(self, path):
        with open(path, 'w') as f:
            f.write(self.translate())
