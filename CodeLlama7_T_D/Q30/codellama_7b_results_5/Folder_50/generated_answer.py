
def insert_before_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == 't':
            new_string += "u" + char
        else:
            new_string += char

    return new_string
