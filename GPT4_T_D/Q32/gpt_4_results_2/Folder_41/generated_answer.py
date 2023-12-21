
def insert_after_character(s):
    new_string = ""
    for char in s:
        if char == 'O':
            new_string += 'Oo'
        else:
            new_string += char
    return new_string
