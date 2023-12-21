
def insert_after_character(string):
    return ''.join([char + "f" if char == "M" else char for char in string])
