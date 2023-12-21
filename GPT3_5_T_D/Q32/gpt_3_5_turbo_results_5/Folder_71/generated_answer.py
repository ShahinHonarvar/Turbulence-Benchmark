
def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == '2':
            new_string += 'S'
    return new_string
