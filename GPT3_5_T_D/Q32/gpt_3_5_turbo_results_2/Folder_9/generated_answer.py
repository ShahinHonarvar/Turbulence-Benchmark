
def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == 'e':
            new_string += 'E'
    return new_string
