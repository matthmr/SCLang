# File Writer

class WRITER: 
    
    start = lambda: print("\n~ START ~\n")
    exit = lambda: print("\n~ EXIT ~\n")
    intro = "\n%s\n<ENTER> + ':q' --> quit program\n<ENTER> + ':s' --> save file\n<ENTER> + ':c' --> initiate/exit cmd mode\n%s" % ("~"*41, "~"*41)

    # parsing :: ends @ 66
    def _parse_(line_content, from_cmd, from_normal, cmd, cmd_ENTRY, from_cmd_time):
        """
        Structure: 

        (line_content, from_cmd, from_normal, cmd, cmd_ENTRY, from_cmd_time) ->
        (`:q`, `cmd`, `cmd_ENTRY`, `from_cmd`, `from_normal`, *`from_cmd_time`)

        obs: line_content is the input
        """

        # Parses with len >= 1   
        if len(line_content) >= 1:

            # <ENTER> in the input
            if line_content[-1][0] == str():

                # in quick cmd mode
                if cmd and not cmd_ENTRY:
                    return True, False, False, False, False, 0
                # in cmd mode
                elif cmd_ENTRY:
                    return True, True, True, False, False, 1
                # in normal mode
                else:
                    return True, True, False, False, False
            
            # <:c> in the input
            elif line_content[-1][0] == ":c":
            # Disabled Sonarlint rule: S1066

                # from cmd mode
                if from_cmd:

                    if from_normal:
                        return True, False, False, False, False

                    elif from_cmd_time == 0:
                        return True, True, True, True, False, 1

                    elif from_cmd_time == 1:
                        return True, False, False, False, False, 0

                # from normal mode
                elif from_normal:
                    # from_cmd = True
                    return True, True, True, True, True
            
            # Tautologies :: if line_content != (":c") or line_content != ("")
            elif cmd and not cmd_ENTRY:
                return True, False, False, False, False, 0
            elif cmd_ENTRY:
                return True, True, True, False, False, 1
            else:
                return True, False, False, False, False

    def _run_(local_str):

        # As defaut
        line, from_cmd_time = 0, 0
        cmd, cmd_ENTRY = False, False
        from_normal, from_cmd = False, False
        _lines_, _cmd_lines_ = list(), list()
        lines, cmd_lines = list(), list()

        # Formating line :: ends @ 101
        def format_str(var:int, cmd, cmd_ENTRY, local_str = local_str):
           
            for _int_ in range(1, local_str + 1):
                
                if len(str(var)) == _int_:
                    return (f"[{var}]" + " "*(local_str - (_int_ - 1))) if cmd or cmd_ENTRY else (f"{var}" + " "*(local_str - (_int_ - 1)) + " "*2)
                
                elif len(str(var)) > local_str:
                    if cmd or cmd_ENTRY:
                        return f"[{var}] "
                    else:
                        for index in [1, 2]:
                            if len(str(var)) == _int_ + index:
                                return f"{var}" + " "*(1 if (index == 2) else 2)
                            else:
                                return f"{var} "
                
        while True:
            # Writing mode w/ lines or cmd_lines

            line += 1
        
            # Writing mode parsing
            # ==============================================
            if cmd_ENTRY:
                obj = WRITER._parse_(cmd_lines, from_cmd, from_normal, cmd, cmd_ENTRY, from_cmd_time)
                cmd, cmd_ENTRY = obj[1], obj[2]
                from_cmd, from_normal = obj[3], obj[4]
                from_cmd_time = obj[5]

            else:

                if cmd and len(cmd_lines) > 0:
                    obj = WRITER._parse_(cmd_lines, from_cmd, from_normal, cmd, cmd_ENTRY, from_cmd_time)
                    cmd, cmd_ENTRY = obj[1], obj[2]
                    from_cmd, from_normal = obj[3], obj[4]
                    from_cmd_time = obj[5]

                elif len(lines) > 0:
                    obj = WRITER._parse_(lines, from_cmd, from_normal, cmd, cmd_ENTRY, from_cmd_time)
                    cmd, cmd_ENTRY = obj[1], obj[2]
                    from_cmd, from_normal = obj[3], obj[4]
            # ==============================================

            # Writing
            # ==============================================
            # cmd writing :: normal writing @ 181
            if cmd:
                
                if cmd_ENTRY:
                    text_and_line_no = (input(format_str(line, cmd, cmd_ENTRY)), line)
                    cmd_lines.append(text_and_line_no)
                    
                    if cmd_lines[-1][0] == ":c":
                        from_cmd = True
                    
                    if cmd_lines[-1][0] == ":s":
                        _lines_ = lines
                        _cmd_lines_ = cmd_lines

                    if cmd_lines[-1][0][:2] == ":d":

                        for index in range(len(lines)):
                            if int(lines[index][1]) == int(cmd_lines[-1][0][3:]):
                                del lines[index]
                                break

                        for index in range(len(cmd_lines)):
                            if int(cmd_lines[index][1]) == int(cmd_lines[-1][0][3:]):
                                del cmd_lines[index]
                                break

                    if cmd_lines[-1][0] == ":q":
                        line += 1
                        print(format_str(line, cmd, cmd_ENTRY) + ":c")
                        cmd_ENTRY = False
                        break
                    
                else:
                    text_and_line_no = (input(format_str(line, cmd, cmd_ENTRY)), line)
                    cmd_lines.append(text_and_line_no)
                    
                    if cmd_lines[-1][0] == ":c":
                        from_cmd = True

                    if cmd_lines[-1][0] == ":s":
                        _lines_ = lines
                        _cmd_lines_ = cmd_lines
                    
                    if cmd_lines[-1][0][:2] == ":d":

                        for index in range(len(lines)):
                            if int(lines[index][1]) == int(cmd_lines[-1][0][3:]):
                                del lines[index]
                                break

                        for index in range(len(cmd_lines)):
                            if int(cmd_lines[index][1]) == int(cmd_lines[-1][0][3:]):
                                del cmd_lines[index]
                                break
                    
                    if cmd_lines[-1][0] == ":q":
                        break

            # normal writing :: cmd writing @ 123
            else:
                text_and_line_no = (input(format_str(line, cmd, cmd_ENTRY)), line)
                lines.append(text_and_line_no)
                if lines[-1][0] == ":c":
                    # cmd, cmd_ENTRY = True, True
                    from_normal = True
            # ==============================================

        if ( _lines_ == list() ) or ( _cmd_lines_ == list() ):
            _lines_ = lines
            _cmd_lines_ = cmd_lines

        line = 0
        del text_and_line_no
        return lines, cmd_lines, _lines_, _cmd_lines_

    def format_file(obj, index):
        return_list = list()

        # tuples are ("CONTENT", line #)
        if index <= 1:

            for tuples in obj[index]:
                if all( (not (tuples[0] == ""), not (tuples[0] == ":c"), not (tuples[0] == ":q"), not (tuples[0] == ":s")) ):
                    return_list.append(tuples[0])
        
        else:

            for tuples in obj[index]:
                if all( (not (tuples[0] == ""), not (tuples[0] == ":c"), not (tuples[0] == ":q"), not (tuples[0] == ":s")) ):
                    return_list.append(tuples[0])
                elif not (tuples[0] == ":s"):
                    break

        return return_list




# todo: save line #'s as a return value
# _lines_ & _cmd_lines_ are saved version of lines & cmd_lines
