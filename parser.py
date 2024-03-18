class Parser:
    def __init__(self, path):
        # open asm file
        self.f = open(path, 'r')
        self.commands = self.f.readlines()
        self.cleanedCommands = []
        self.curIndex = -1

        # clean commands
        self.cleanCommands()

    def cleanCommands(self):
        for command in self.commands:
            if command[:2] == '//' or command[0] == '\n':
                continue
            else:
                command = command.replace(' ', '')
                self.cleanedCommands.append(command)

    def hasMoreCommands(self):
        return self.curIndex < len(self.cleanedCommands) - 1

    def advance(self):
        self.curIndex += 1

    def commandType(self):
        if self.cleanedCommands[self.curIndex][0] == '@':
            return 'A_COMMAND'
        elif self.cleanedCommands[self.curIndex][0] == '(':
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'

    def symbol(self):
        if self.commandType() == 'A_COMMAND':
            return self.cleanedCommands[self.curIndex][1:]
        elif self.commandType() == 'L_COMMAND':
            return self.cleanedCommands[self.curIndex][1:-1]
        else:
            return 'null'

    def dest(self):
        if self.commandType() == 'C_COMMAND':
            endIdx = self.cleanedCommands[self.curIndex].find('=')
            if endIdx == -1:
                return 'null'
            return self.cleanedCommands[self.curIndex][:endIdx]

    def comp(self):
        if self.commandType() == 'C_COMMAND':
            startIdx = self.cleanedCommands[self.curIndex].find('=') + 1
            endIdx = self.cleanedCommands[self.curIndex].find(';')

            return self.cleanedCommands[self.curIndex][startIdx:endIdx]

    def jump(self):
        if self.commandType() == 'C_COMMAND':
            startIdx = self.cleanedCommands[self.curIndex].find(';')
            if startIdx == -1:
                return 'null'

            # print(self.cleanedCommands[self.curIndex][startIdx + 1:])

            return self.cleanedCommands[self.curIndex][startIdx + 1:-1]
