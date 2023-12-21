
def insert_before_character(string, character):
    new_string = ""
    for i in range(len(string)):
        if string[i] == character:
            new_string += "U" + string[i]
        else:
            new_string += string[i]
    return new_string
