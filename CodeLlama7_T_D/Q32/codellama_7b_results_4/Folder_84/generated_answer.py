
def insert_after_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == "H":
            new_string += "n" + char
        else:
            new_string += char

    return new_string
