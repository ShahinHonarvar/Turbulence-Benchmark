
def insert_after_character(string):
    return ''.join([char + '6' if char == 'X' else char for char in string])
