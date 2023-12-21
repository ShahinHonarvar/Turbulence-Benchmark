
def insert_after_character(s):
    new_str = ''
    for char in s:
        if char == 'i':
            new_str += 'iI'
        else:
            new_str += char
    return new_str
