
def insert_after_character(string):
    new_string = ""
    for character in string:
        new_string += character
        if character == 'a':
            new_string += 't'
    return new_string
