
def insert_before_character(s, c):
    return ''.join([c + 'l' if x == c else x for x in s])
