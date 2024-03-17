class Parser:
    def __init__(self, path):
        # open asm file
        self.f = open(path, 'r')
        self.commands = self.f.readlines()
        self.cleanedCommands = []

        # clean commands
        self.cleanCommands()

    def cleanCommands(self) -> None:
        for command in self.commands:
            if command[:2] == '//' or command[0] == '\n':
                continue
            else:
                self.cleanedCommands.append(command)

    def hasMoreCommands(self) -> bool:
        return len(self.cleanedCommands) > 0

    def advance(self) -> None:
        self.cleanedCommands.pop(0)

    def commandType(self) -> str:
        if self.cleanedCommands[0][0] == '@':
            return 'A_COMMAND'
        elif self.cleanedCommands[0][0] == '(':
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'

    def symbol(self) -> str | None:
        if self.commandType() == 'A_COMMAND':
            return self.cleanedCommands[0][1:]
        elif self.commandType() == 'L_COMMAND':
            return self.cleanedCommands[0][1:-1]
        else:
            return None

    def dest(self) -> str | None:
        if self.commandType() == 'C_COMMAND':
            endIdx = self.cleanedCommands[0].find('=')
            if endIdx == -1:
                return None

            return self.cleanedCommands[0][:endIdx]

    def comp(self) -> str | None:
        if self.commandType() == 'C_COMMAND':
            startIdx = self.cleanedCommands[0].find('=')
            endIdx = self.cleanedCommands[0].find(';')
            if endIdx == -1:
                return None

            return self.cleanedCommands[0][startIdx+1:endIdx]

    def jump(self) -> str | None:
        if self.commandType() == 'C_COMMAND':
            startIdx = self.cleanedCommands[0].find(';')
            if startIdx == -1:
                return None

            return self.cleanedCommands[0][:startIdx]

    def showCommands(self) -> None:
        print(f"\n Original Commands: {self.commands} \n")
        print(f"Cleaned Commands: {self.cleanedCommands} \n")
