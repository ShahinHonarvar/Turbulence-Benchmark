
def insert_after_character(str):
    new_str = ""
    for char in str:
        new_str += char
        if char == 'A':
            new_str += 'H'
    return new_str
