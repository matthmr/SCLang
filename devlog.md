# DevLog: 26/03/21

## Bugs
- [x] Writer not exit when entering command mode via ":c"
- [x] Writer not exit when entering command mode via "<ENTER>"

## Work
- [ ] Work on syntax module/interpreter

## Notes
- :d in ./writer/scWRITER is working as of this devlog.
- ./writer/scWRITER.WRITER has two important functions:
	> `_parse_`, which parses the input and identifies cmd entrance and such. It returns `bool` type. 
	> `_run_.format_str`, which deals with string formating, aka line length.

## Vars
> `cmd_ENTRY` is bounded to `cmd`, but not vice-versa.
> `cmd` is the _boolean_ value for <ENTER> in the input, while `cmd_ENTRY` is the _boolean_ value for the <:c> in the input **entering** cmd mode.
> `from_normal` is the _boolean_ value for entering cmd mode via normal mode, while `from_cmd` is the _boolean_ value for entering cmd mode via quick cmd mode.
> `from_normal_time` has a limit of 2.

## Todo:
- Work on syntax module/interpreter.

---

# DevLog 27/03/21

## Work

- [ ] Improve the GUI

