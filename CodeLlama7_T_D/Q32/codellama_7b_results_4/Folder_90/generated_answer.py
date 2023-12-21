
def insert_after_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == 'U':
            new_string += 'F' + char
        else:
            new_string += char

    return new_string
