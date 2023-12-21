
def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'U':
            new_string += 'q' + char
        else:
            new_string += char
    return new_string
