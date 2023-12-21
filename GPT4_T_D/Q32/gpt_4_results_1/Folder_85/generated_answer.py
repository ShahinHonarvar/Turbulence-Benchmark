
def insert_after_character(s):
    new_s = ''
    for character in s:
        new_s += character
        if character == 'o':
            new_s += 'a'
    return new_s
