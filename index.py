from assembler import Assembler
import sys

# D:/USER/PATH/Prog.asm
if len(sys.argv) < 2:
    print("Usage: python index.py <path>")
    sys.exit(1)

try:
    assembler = Assembler(sys.argv[1])
    assembler.populateSymbolTableLCmds()
    assembler.populateSymbolTableACmds()
    assembler.writeFile(sys.argv[1].split(".")[0] + ".hack")

    print("Translated file successfully written to " +
          sys.argv[1].split(".")[0] + ".hack")
except Exception as e:
    print(e)
