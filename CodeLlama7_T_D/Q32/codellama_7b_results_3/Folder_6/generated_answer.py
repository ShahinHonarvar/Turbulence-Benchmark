
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "X":
            new_string += "u"
        new_string += string[i]
    return new_string
