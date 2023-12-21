
def insert_after_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == "P":
            new_string += "V" + char
        else:
            new_string += char

    return new_string
