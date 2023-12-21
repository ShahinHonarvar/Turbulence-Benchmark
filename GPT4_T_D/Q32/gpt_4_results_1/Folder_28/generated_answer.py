
def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == 'r':
            new_string += '1'
    return new_string
