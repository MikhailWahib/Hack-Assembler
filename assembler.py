from parser import Parser
from code import Code


class Assembler:

    def __init__(self, path):
        self.parser = Parser(path)
        self.code = Code()
        self.translated = ""

    def toBinary(self, num):
        return bin(int(num))[2:].zfill(16)

    def translate(self):
        while self.parser.hasMoreCommands():
            self.parser.advance()
            if self.parser.commandType() == "A_COMMAND":
                self.translated += self.toBinary(self.parser.symbol())
                self.translated += '\n'

            elif self.parser.commandType() == "C_COMMAND":
                res = '111'
                dest = self.code.dest(self.parser.dest())
                comp = self.code.comp(self.parser.comp())
                jump = self.code.jump(self.parser.jump())
                # print(self.parser.dest(), self.parser.comp(), self.parser.jump())

                res += comp + dest + jump + '\n'
                self.translated += res

        return self.translated

    def writeFile(self, path):
        with open(path, 'w') as f:
            f.write(self.translate())


t = Assembler(
    "INPUT PATH HERE")

print(t.translate())

t.writeFile("OUTPUT PATH HERE")
