
def insert_after_character(string):
    new_string = ""
    for char in string:
        new_string += char
        if char == 'C':
            new_string += 'Z'
    return new_string
