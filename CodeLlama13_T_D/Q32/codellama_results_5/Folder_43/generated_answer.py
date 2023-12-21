
def insert_after_character(string):
    return ''.join([char if char != 'G' else f'{char}t' for char in string])
