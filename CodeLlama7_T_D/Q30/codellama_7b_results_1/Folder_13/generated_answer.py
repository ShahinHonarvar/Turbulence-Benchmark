
def insert_before_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "N" and string[i-1] == "x":
            new_string += string[:i] + "N" + string[i:]
    return new_string
