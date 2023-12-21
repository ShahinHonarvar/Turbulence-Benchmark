
def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == 'S':
            new_string += 'U'
    return new_string
