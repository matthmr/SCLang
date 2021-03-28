# Syntax module for SC

# Default values for closing quotes: 4, 11, 17
# 1st Euler Difference: 7, 6 

# Formats uSettings.txt for data
def format_to_uSettings(os = None, ll = None, iol = None):

    if not (os is None) and not (ll is None) and not (iol is None):
        return f"OS=<{os}>\nIOL=<{iol}>\nLL=<{ll}>"
    
    elif not (os is None) and not (ll is None) and (iol is None):
        return f"OS=<{os}>\nIOL=<>\nLL=<{ll}>"  

    elif not (os is None) and (ll is None) and not (iol is None):
        return f"OS=<{os}>\nIOL=<{iol}>\nLL=<>"

    elif not (os is None) and (ll is None) and (iol is None):
        return f"OS=<{os}>\nIOL=<>\nLL=<>"
    
    elif (os is None) and not (ll is None) and not (iol is None):
        return f"OS=<>\nIOL=<{iol}>\nLL=<{ll}>"
    
    elif (os is None) and not (ll is None) and (iol is None):
        return f"OS=<>\nIOL=<>\nLL=<{ll}>"

    elif (os is None) and (ll is None) and not (iol is None):
        return f"OS=<>\nIOL=<{iol}>\nLL=<>"

    else:
        return "OS=<>\nIOL=<>\nLL=<>"

# Opens the file on-demand
def open_file():
    
    with open("uSettings.txt", "r") as file:
        file = list(file.read())
    
    return file

# Parser for OS, IOL and LL identification
class from_uSettings:
    """
    The values of char, char2 & char3 are the (py) indices for the closing quotes.
    The dafault closing values (aka if there's no data in any of them) is 4, 11, 17.
    """

    return_list = list()
    return_index = tuple()
    local_str = str()
    file = open_file()

    # OS
    if file[(index := 4)] == ">":
        return_list.append(None)
        return_index += (index, )
        local_str = str()
    else:
        while True:
            local_str += file[index]
            index += 1

            if file[index] == ">":
                return_list.append(local_str)
                return_index += (index, )
                local_str = str()
                break
    # IOL
    if file[(index := return_index[0] + 7)] == ">":
        return_list.append(None)
        return_index += (index, )
        local_str = str()
    else:
        while True:
            local_str += file[index]
            index += 1

            if file[index] == ">":
                return_list.append(local_str)
                return_index += (index, )
                local_str = str()
                break

    # LL
    if file[(index := return_index[1] + 6)] == ">":
        return_list.append(None)
        return_index += (index, )
        local_str = str()
    else:
        while True:
            local_str += file[index]
            index += 1

            if file[index] == ">":
                return_list.append(local_str)
                return_index += (index, )
                local_str = str()
                break

    data = return_list

    # fetch_os, fetch_iol & fetch_ll give the index of the closing quote
    fetch_os = return_index[0]
    fetch_iol = return_index[1] 
    fetch_ll = return_index[2]

# SC Syntax
class Syntax:
        
    def CellsOf(_code_):

        _cells_ = list()
        temp_char, formated_temp_char = str(), str()

        for _code_line_ in _code_:

            formated_temp_char, temp_char = str(), str()

            for index in range(len(_code_line_)):

                temp_char += _code_line_[index]

                # Checks for valid cells
                if temp_char[-1] == ";" and temp_char[0] == " ":

                    # Checks for ending cell
                    if index < (len(_code_line_) - 1):

                        if _code_line_[index + 1] == ";":
                            temp_char += ";"
                            for char in temp_char:
                                if char == " ":
                                    pass
                                else:
                                    formated_temp_char += char
                            
                            if formated_temp_char:
                                _cells_.append(formated_temp_char)

                            temp_char, formated_temp_char = str(), str()

                    # Checks for normal cell
                    for char in temp_char:
                        if char == " ":
                            pass
                        else:
                            formated_temp_char += char
                    
                    if formated_temp_char:
                        _cells_.append(formated_temp_char)
                    
                    temp_char, formated_temp_char = str(), str()
            
                # Excepts the case of trailing
                elif temp_char[-1] == ";" and temp_char[0] == _code_line_[0]:
                    if temp_char:
                        _cells_.append(temp_char)

                    temp_char = str()
            
        if not _cells_:
            return
            # returns None if there are no cells

        else:
            return _cells_
