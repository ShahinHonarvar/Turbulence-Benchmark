
def insert_before_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == "0":
            new_string += "H" + char
        else:
            new_string += char

    return new_string
