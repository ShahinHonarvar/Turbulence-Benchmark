
def insert_after_character(string):
    return ''.join('X' + char if char == ' ' else char for char in string)
