# Debugging
from writer.sc_writer import WRITER as File
from os import system

formating = 3

while True:
    try:
        file = File._run_(formating)
        # print("\ncmd, cmd_ENTRY:", (File._run_.cmd, File._run_.cmd_ENTRY))
    except KeyboardInterrupt:
        try:
            print("\nFile:", file[0], "\n")
        except NameError:
            break
        # system("clear")
        break

