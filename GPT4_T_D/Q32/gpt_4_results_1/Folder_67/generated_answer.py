
def insert_after_character(string):
    modified_string = ""
    for character in string:
        if character == 'j':
            modified_string += 'j1'
        else:
            modified_string += character
    return modified_string
