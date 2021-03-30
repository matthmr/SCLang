## This is a *SC* [*semi-colon*] compiler, interpreter and debugger.

- The ENTIRE language is compiled into some few Python files; utilizing only built-in Python modules, such as sqlite3, and some *clever programming* to make the language a bit more optimized, besides also using a *different approach* to programming that Python.

- There's no current tutorial of SC as of this version, however some __documentations__ are to come!

## How to run it?

- To run it you'll have to install python on your machine, if you don't know where to download click [here](https://www.python.org/downloads/), after installing python into `path`, open `cmd.exe` in *administrator mode* and run:

```bash
C:\Windows\System32> cd %PATH_TO_SCLang%
C:\%PATH%> python sc_ui.py
```

## What commands do I have?

- There are *two* main modes in `sc_ui.py`: **debug**/**exec** and **writing**. In the first one, besides `:q`, `:c` & `:w`, there are *three* more commands:

1. `:cos #`

2. `:cis #`

3. `:cfs #`

( where "#" is an *integer*)

1. Changes the `os` value, which can also be changed by modifying the value of it between <> in `uSettings.txt`, so that the program optimizes to your specific `os`. Values available are: `:cos windows`, `:cos linux` &`:cos android`.
2. Changes the `iol` value, which can also be changed by modifying the value of it between <> in `uSettings.txt`. `iol`controls the **spacing** of the **I/O** values for both languages in the debugger.
3. Changes the `ll` value, which can also be changed by modifying the value of it between <> in `uSettings.txt`. `ll` controls the **spacing** of the **lines** in **writing mode**.

- There is *one* command in writing mode, besides `:q`, `:s` & `:c`, `:d #` (where "#" is an integer). `:d` deletes whichever line has the value of `#`.

The files named "writer.cmd_file.txt" & "writer.file.txt" are only there for stability for WSL Ubuntu (which was the one I used for debugging and coding the program in the most part). It's harmless to delete for the program is going to create one again (if necessary).

## Development

- If the language is still in dev, you can find videos of it [here](https://www.youtube.com/channel/UCyCzRQMfOjHoXrjXvzKKROQ) & [here](https://www.twitch.tv/mhummerr).

## Notes

- The file "sc_debug.py" is harmless and only used by the devs to debug parts of the program without having to initialize the main ("sc_ui.py") file.
