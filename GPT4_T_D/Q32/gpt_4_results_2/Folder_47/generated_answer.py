
def insert_after_character(s):
    new_s = ""
    for char in s:
        new_s += char
        if char == 'E':
            new_s += 'f'
    return new_s
