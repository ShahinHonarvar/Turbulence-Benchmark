
def insert_after_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == "S":
            new_string += "U" + char
        else:
            new_string += char

    return new_string
