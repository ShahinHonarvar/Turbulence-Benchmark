
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == " ":
            new_string += "o" + string[i]
        else:
            new_string += string[i]
    return new_string
