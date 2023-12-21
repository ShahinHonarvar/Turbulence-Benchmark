
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "w":
            new_string += "n"
        new_string += string[i]
    return new_string
