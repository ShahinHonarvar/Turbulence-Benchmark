
def insert_after_character(string):
    new_string = ""
    for char in string:
        if char == 'N':
            new_string += char + 'j'
        else:
            new_string += char
    return new_string
