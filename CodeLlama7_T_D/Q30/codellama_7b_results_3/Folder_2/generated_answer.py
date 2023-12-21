
def insert_before_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == 'C':
            new_string += "Z" + char
        else:
            new_string += char

    return new_string
