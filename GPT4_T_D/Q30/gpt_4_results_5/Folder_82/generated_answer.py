
def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'I':
            new_string += 'I'
        new_string += char
    return new_string
