
def insert_after_character(string):
    new_string = ""
    for char in string:
        new_string += char
        if char == 'i':
            new_string += 'I'
    return new_string
