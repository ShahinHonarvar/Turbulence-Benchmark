
def insert_before_character(string):
    new_string = ""
    for char in string:
        if char == 'k':
            new_string += 'k'
        new_string += char
    return new_string
