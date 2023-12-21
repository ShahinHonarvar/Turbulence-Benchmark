
def insert_after_character(string):
    new_string = ""
    for i, char in enumerate(string):
        if char == 'E':
            new_string += char + 'E'
        else:
            new_string += char

    return new_string
