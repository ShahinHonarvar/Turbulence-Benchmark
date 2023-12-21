
def insert_before_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "0":
            new_string += "0"
        elif string[i] == "i":
            new_string += "0" + "i"
        else:
            new_string += string[i]
    return new_string
