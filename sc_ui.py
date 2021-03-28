# Local imports
from writer.sc_writer import WRITER as File
from syntax.sc_syn import from_uSettings, format_to_uSettings, Syntax

# Python imports
# import logging
from os import system

# Data from uSettings
data = from_uSettings.data

# Ensure data values
if data[2] is None:
    data[2] = 2

if data[0] is None:
    print("="*18, "This code will run only once", "="*18)
    data[0] = input("Input the OS you're currently in (e.g. windows, linux): ")

if data[1] is None:
    print("="*18, "This code will run only once", "="*18)
    data[1] = int(input("Input the number of spaces for indentation of the debugger: "))

# Ensure str -> int
data[1] = int(data[1])
data[2] = int(data[2])

# As default
lang, temp_lang = "Python", "SC"
_lang_python_, _lang_SC_= [0, 0], [0, 0]
_IO_lang_python_, _IO_lang_SC_ = list(), list()
time, debug = 0, str()

# Formating string function
def format_io(input_no:int, var:str, iol = data[1]) -> str:
    """
    input_no :: Integer number of I/O #
    var      :: I/O content
    iol      :: Spacing
    """

    if len(str(input_no)) > iol:
        return (var + " ")

    else:
        for _int_ in range(1, iol + 1):
            if len(str(input_no)) == _int_:
                return (var + " "*(iol - (_int_ - 1)))


# System commands
if data[0].upper() == "LINUX" or data[0].upper() == "ANDROID":
    system("clear")

elif data[0].upper() == "WINDOWS":
    system("title SC Debugger")
    system("cls")

# logging.basicConfig(filename="sclog.log", encoding="utf-8")

class Input:
    """
    _mode_() = In
    _mode_(True) = Out
    """

    _mode_ = lambda _hasExec_ = False: "Out" if _hasExec_ else "In "

    def _io_no_(_lang_):
        """
        _lang_{LANG HERE}_[0] = Input value
        _lang_{LANG HERE}_[1] = Output value
        """
        global _lang_python_, _lang_SC_
        if _lang_ == "Python" and _lang_python_[0] == _lang_python_[1]:
            _lang_python_[0] += 1
            return _lang_python_
        elif _lang_ == "Python" and _lang_python_[0] - _lang_python_[1] == 1:
            _lang_python_[1] += 1
            return _lang_python_
        elif _lang_ == "SC" and _lang_SC_[0] == _lang_SC_[1]:
            _lang_SC_[0] += 1
            return _lang_SC_
        elif _lang_ == "SC" and _lang_SC_[0] - _lang_SC_[1] == 1:
            _lang_SC_[1] += 1
            return _lang_SC_

class Log:
    global lang, _IO_lang_python_, _IO_lang_SC_
    py = _IO_lang_python_
    sc = _IO_lang_SC_

    def __init__(self, _code_, lang):
        if lang == "Python":
            self.appendPy = self.py.append(_code_)
            self.debugPy = "Python"
        elif lang == "SC":
            self.appendSC = self.sc.append(_code_)
            self.debugSC = "SC"

    getPy = lambda ioN: print(_IO_lang_python_[ioN - 1])
    getSC = lambda ioN: print(_IO_lang_SC_[ioN - 1])

class Ensure:
    """
    Ensure.quit & Ensure.write both return False if 
    the code is what they're intended to identify.
    """
    
    def out(code, lang):
        if code == ":c" and lang == "Python":
            return "SC"
        elif code == ":c" and lang == "SC":
            return "Python"
        else:
            return lang
    
    def quit(code):
        if code == ":q":
            return False
        else:
            return True
    
    def write(code):
        if code == ":w":
            return False
        else:
            return True

    def change_os(code):
        if code[:4] == ":cos":
            return False
        else:
            return True

    def change_writer_formating(code):
        if code[:4] == ":cfs":
            return False
        else:
            return True

    def change_io_formating(code):
        if code[:4] == ":cis":
            return False
        else:
            return True

# main function

def run():
    global time

    mode = input("%s\n|Press ENTER to start debugging...      |\n%s\n|Press CTRL-C to exit the program...    |\n%s\n\n\n%s\n':q' --> quit program\n':c' --> change debugger\n':w' --> write file mode (SC)\n%s\n" % ("="*41, "="*41, "="*41, "~"*41, "~"*41))

    if not mode:
        pass
    else:
        while True:
            mode = input("\nNot valid. Please input either ENTER or CTRL-C\n")
            if not mode:
                break
            else:
                continue

    print("\n<Starting debug session in the python language>\n\n")
    
    def QueryRun():
        global lang, temp_lang, time, debug, data, _lang_SC_, _lang_python_
        # :: "python", "sc", 0, "", [None, None, None], [0, 0], [0, 0] :: #

        while Ensure.quit(debug):
            
            # Input value
            debug = input(format_io(_lang_SC_[0] + 1, f"<{lang}>     {Input._mode_()}[{Input._io_no_(lang)[0]}]:", data[1]) if lang == "SC" else format_io(_lang_python_[0] + 1, f"<{lang}> {Input._mode_()}[{Input._io_no_(lang)[0]}]:", data[1]))

            temp_lang = lang
            lang = Ensure.out(debug, lang)

            # Changing
            if lang == "SC" and temp_lang == "Python":

                print(format_io(_lang_SC_[1] + 1, f"<{temp_lang}>     {Input._mode_(True)}[{Input._io_no_(temp_lang)[1]}]:", data[1]) if temp_lang == "SC" else format_io(_lang_python_[1] + 1, f"<{temp_lang}> {Input._mode_(True)}[{Input._io_no_(temp_lang)[1]}]:", data[1]), end="")
                print("<Changed from %s to %s>" % (temp_lang, lang))
                Log("<Changed from %s to %s>" % (temp_lang, lang), temp_lang).appendPy
                continue
            
            elif lang == "Python" and temp_lang == "SC":

                print(format_io(_lang_SC_[1] + 1, f"<{temp_lang}>     {Input._mode_(True)}[{Input._io_no_(temp_lang)[1]}]:", data[1]) if temp_lang == "SC" else format_io(_lang_python_[1] + 1, f"<{temp_lang}> {Input._mode_(True)}[{Input._io_no_(temp_lang)[1]}]:", data[1]), end="")
                print("<Changed from %s to %s>" % (temp_lang, lang))
                Log("<Changed from %s to %s>" % (temp_lang, lang), temp_lang).appendSC
                continue

            # Ensuring
            if not Ensure.quit(debug):
                print("\n\n<Program exited successfully...>\n")
                continue

            if not Ensure.change_os(debug):
                temp = data[0]
                print(format_io(_lang_SC_[1] + 1, f"<{lang}>     {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]) if lang == "SC" else format_io(_lang_python_[1] + 1, f"<{lang}> {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]), end="")

                if (debug[4:] == " "*( len(debug) - 4 )):
                    print(f"<Current OS is: {data[0]}>")

                    if lang == "Python":
                        Log(f"<Current OS is: {data[0]}>", lang).appendPy
                    else:
                        Log(f"<Current OS is: {data[0]}>", lang).appendSC
                    
                    continue

                elif len(debug) >= 5:

                    if data[0].upper() == debug[5:].upper():
                        print("<Invalid command: same OS>")
                        if lang == "Python":
                            Log("<Invalid command: same OS>", lang).appendPy
                        else:
                            Log("<Invalid command: same OS>", lang).appendSC

                        continue

                    else:
                        data[0] = debug[5:]
                        print(f"<OS changed from {temp} to {data[0]}>")
                        
                        if lang == "Python":
                            Log(f"<OS changed from {temp} to {data[0]}>", lang).appendPy
                        else:
                            Log(f"<OS changed from {temp} to {data[0]}>", lang).appendSC

                        del temp
                        continue

            if not Ensure.change_io_formating(debug):
                temp = data[1]
                print(format_io(_lang_SC_[1] + 1, f"<{lang}>     {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]) if lang == "SC" else format_io(_lang_python_[1] + 1, f"<{lang}> {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]), end="")

                if (debug[4:] == " "*( len(debug) - 4 )):
                    print(f"<Current formating is: {data[1]}>")

                    if lang == "Python":
                        Log(f"<Current formating is: {data[1]}>", lang).appendPy
                    else:
                        Log(f"<Current formating is: {data[1]}>", lang).appendSC

                    continue

                elif len(debug) >= 5:

                    if data[1] == int(debug[5:]):
                        print("<Invalid command: same formating>")
                        if lang == "Python":
                            Log("<Invalid command: same formating>", lang).appendPy
                        else:
                            Log("<Invalid command: same formating>", lang).appendSC

                        continue

                    else:

                        data[1] = int(debug[5:])
                        print(f"<Formating changed from {temp} to {data[1]}>")
                        
                        if lang == "Python":
                            Log(f"<Formating changed from {temp} to {data[1]}>", lang).appendPy
                        else:
                            Log(f"<Formating changed from {temp} to {data[1]}>", lang).appendSC

                        del temp
                        continue

            if not Ensure.change_writer_formating(debug):
                temp = data[2]
                print(format_io(_lang_SC_[1] + 1, f"<{lang}>     {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]) if lang == "SC" else format_io(_lang_python_[1] + 1, f"<{lang}> {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]), end="")

                if (debug[4:] == " "*( len(debug) - 4 )):
                    print(f"<Current line length is: {data[2]}>")

                    if lang == "Python":
                        Log(f"<Current line length is: {data[2]}>", lang).appendPy
                    else:
                        Log(f"<Current line length is: {data[2]}>", lang).appendSC
                    
                    continue

                elif len(debug) >= 5:

                    if data[2] == int(debug[5:]):
                        print("<Invalid command: same line number>")
                        if lang == "Python":
                            Log("<Invalid command: same line number>", lang).appendPy
                        else:
                            Log("<Invalid command: same line number>", lang).appendSC

                        continue

                    else:

                        data[2] = int(debug[5:])
                        print(f"<Line length changed from {temp} to {debug[5:]}>")
                        
                        if lang == "Python":
                            Log(f"<Line length changed from {temp} to {debug[5:]}>", lang).appendPy
                        else:
                            Log(f"<Line length changed from {temp} to {debug[5:]}>", lang).appendSC

                        del temp
                        continue
            # Writing
            if not Ensure.write(debug):

                if lang == "Python":
                    print(format_io(_lang_python_[1] + 1, f"<{lang}> {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]))
                    print("<Invalid command: Writing Mode is not allowed in Python, only SC>")
                    Log("<Invalid command: Writing Mode is not allowed in Python, only SC>", lang).appendPy
                    Input._io_no_(lang)
                    continue

                elif lang == "SC":
                    print(format_io(_lang_SC_[1] + 1, f"<{lang}>     {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]), end="")
                    print("<Starting Writing Mode in the SC language>")
                    Log("<Starting Writing Mode in the SC language>", lang).appendSC
                    
                    if not time:
                        print(File.intro)
                    
                    time += 1

                    File.start()
                    obj = File._run_(data[2])
                    File.exit()

                    # Formating Writing
                    file = File.format_file(obj, 0)
                    cmd_file = File.format_file(obj, 1)
                    saved_file = File.format_file(obj, 2)
                    saved_cmd_file = File.format_file(obj, 3)
                    
                    # Writing to file
                    with open(".\\writer\\file.txt", "w+") as f:
                        for line in file:
                            f.write(line)
                            f.write("\n")
                    with open(".\\writer\\cmd_file.txt", "w+") as f:
                        for cmd_line in cmd_file:
                            f.write(cmd_line)
                            f.write("\n")

                    del f, obj
                    continue

            # Executing
            if lang == "Python":
                
                print(format_io(_lang_SC_[1] + 1, f"<{lang}> {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]) if lang == "SC" else format_io(_lang_python_[1] + 1, f"<{lang}> {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]), end="")
                Log(debug, lang).appendPy

                if debug[:5] == "print":
                    if len(debug) > 5:
                        try:
                            exec(debug)
                        except:
                            print("<Invalid command: not a system command>")
                    else:
                        try:
                            exec("print(" + debug + ")")
                        except:
                            print("<Invalid command: not a system command>")

                else:
                    try:
                        exec("print(" + debug + ")")
                    except:
                        print("<Invalid command: not a system command>")

            elif lang == "SC":
                Log(debug, lang).appendSC
                                
                if debug[:4] == ":scx":
                    # scx exec

                    print(format_io(_lang_SC_[1] + 1, f"<{lang}>     {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]) if lang == "SC" else format_io(_lang_python_[1] + 1, f"<{lang}>     {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]), end="")

                    # return value; debugging
                    Cells = Syntax.CellsOf(file)
                    
                    # Debug
                    print(Cells)
                    
                    continue
               
                elif debug[:5] == ":sc++":
                    # sc++ exec
                    
                    print(format_io(_lang_SC_[1] + 1, f"<{lang}>     {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]) if lang == "SC" else format_io(_lang_python_[1] + 1, f"<{lang}>     {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]), end="")
                    print("IN DEV")

                    continue
                
                elif debug[:3] == ":sc":
                    # sc exec
                    
                    print(format_io(_lang_SC_[1] + 1, f"<{lang}>     {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]) if lang == "SC" else format_io(_lang_python_[1] + 1, f"<{lang}>     {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]), end="")
                    print("IN DEV")
                    continue

                else:
                    print(format_io(_lang_SC_[1] + 1, f"<{lang}>     {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]) if lang == "SC" else format_io(_lang_python_[1] + 1, f"<{lang}>     {Input._mode_(True)}[{Input._io_no_(lang)[1]}]:", data[1]), end="")
                    print("IN DEV")
                    continue
    
    return QueryRun

if __name__ == "__main__":
    main = run()
    main()

    # Saving uSettings
    with open("uSettings.txt", "w+") as f:
        f.write(format_to_uSettings(os = data[0],
            iol = data[1],
            ll = data[2])
        )

# System commands
if data[0].upper() == "WINDOWS":
    system("title Command Prompt")
    system("cls")
elif data[0].upper() == "LINUX" or data[0].upper() == "ANDROID":
    system("clear")
