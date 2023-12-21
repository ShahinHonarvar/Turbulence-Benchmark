
def insert_after_character(string):
    new_string = ""
    for char in string:
        new_string += char
        if char == 'A':
            new_string += 'a'
    return new_string
