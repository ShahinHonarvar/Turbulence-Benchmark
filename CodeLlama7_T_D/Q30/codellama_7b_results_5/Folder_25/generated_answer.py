
def insert_before_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "e":
            new_string += "W" + string[i]
        else:
            new_string += string[i]
    return new_string
