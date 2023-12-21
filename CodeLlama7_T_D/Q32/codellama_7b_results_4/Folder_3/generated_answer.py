
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "0":
            new_string += "H" + string[i+1:]
    return new_string
