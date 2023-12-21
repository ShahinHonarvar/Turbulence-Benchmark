
def insert_after_character(string):
    return ''.join([char + '5' if char == ' ' else char for char in string])
