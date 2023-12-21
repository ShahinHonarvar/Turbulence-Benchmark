
def insert_before_character(str):
    new_str = ''
    for char in str:
        if char == 's':
            new_str += 'w'
        new_str += char
    return new_str
