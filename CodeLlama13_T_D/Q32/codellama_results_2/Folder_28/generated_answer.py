
def insert_after_character(string):
    return "".join([char + "1" if char == 'r' else char for char in string])
