
def insert_before_character(string):
    return ''.join(['Q' + char if char == 'm' else char for char in string])
