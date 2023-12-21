
def insert_after_character(string):
    modified_string = ""
    for char in string:
        modified_string += char
        if char == 'e':
            modified_string += 'e'
    return modified_string
