
def insert_before_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "E":
            new_string += "e" + string[i]
        else:
            new_string += string[i]
    return new_string
