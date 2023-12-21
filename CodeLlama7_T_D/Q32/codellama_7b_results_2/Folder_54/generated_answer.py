
def insert_after_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == "M":
            new_string += "f" + char
        else:
            new_string += char

    return new_string
