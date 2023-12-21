
def insert_after_character(string):
    return ''.join(char + 'n' if char == 'H' else char for char in string)
