
def insert_after_character(string):
    new_string = ""
    for i in range(len(string)):
        if string[i].lower() == "e":
            new_string += string[i] + "E"
        else:
            new_string += string[i]
    return new_string
