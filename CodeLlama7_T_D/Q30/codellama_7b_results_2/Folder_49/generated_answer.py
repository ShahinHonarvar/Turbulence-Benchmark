
def insert_before_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "i":
            new_string += "i"
            if i + 1 < len(string) and string[i + 1] == "i":
                new_string += "i"
        else:
            new_string += string[i]
    return new_string
