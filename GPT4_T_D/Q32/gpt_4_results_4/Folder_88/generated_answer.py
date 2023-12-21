
def insert_after_character(s):
    new_string = ''
    for char in s:
        if char == 'a':
            new_string += char + 't'
        else:
            new_string += char
    return new_string
