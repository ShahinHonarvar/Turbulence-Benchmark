
def insert_before_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "k":
            new_string += "k" + string[i]
        else:
            new_string += string[i]
    return new_string
