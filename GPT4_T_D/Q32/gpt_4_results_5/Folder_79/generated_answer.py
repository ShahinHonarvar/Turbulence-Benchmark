
def insert_after_character(string):
    new_string = ''
    for character in string:
        new_string += character
        if character == 'E':
            new_string += 'E'
    return new_string
