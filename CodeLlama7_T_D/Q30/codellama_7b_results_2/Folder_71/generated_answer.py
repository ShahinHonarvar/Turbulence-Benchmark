
def insert_before_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == "2":
            new_string += "S" + char
        else:
            new_string += char

    return new_string
