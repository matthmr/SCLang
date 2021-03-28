This is a SC [semi-colon] compiler and debugger.

The ENTIRE language is compiled into some few Python files; utilising only built-in Python modules, such as sqlite3, and some *clever programming*.

There's no current tutorial of SC as of (5:18 AM 5/3/2021), however some __doc__ string documentations are to come!

Although the ENTIRE programming language is compiled into some Python files, the performance and optimisation are fine for the language uses a different approach to programming than Python's.

Run the "scGUI.py" file in terminal to execute the debugger and/or SC/Python writting. Use the command ":cos " + "your system here" to especify which OS you're currently on. Doing that will optimize the program to work better on your OS.

The files named "writer.cmd_file.txt" & "writer.file.txt" are only there for stability for WSL Ubuntu (which was the one I used for debugging and coding the program in the most part). It's harmless to delete for the program is going to create one again (if necessary).

The file "scDEBUG.py" is harmless and only used to debug parts of the program without having to initialize the main ("scGUI.py") file.

[REMEMBER TO DOWNLOAD THE FILES **ONLY** FROM GITHUB!!]

# --- Methods that work ---
    importing
    exec((open(".\\syntax\\scPARSER.py", "r").read()).close())
    system("python .\\syntax\\scPARSER.py")
    import runpy runpy.run_path(path_name='.\\syntax\\scPARSER.py')