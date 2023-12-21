
def insert_before_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == "u":
            new_string += "U" + char
        else:
            new_string += char

    return new_string
