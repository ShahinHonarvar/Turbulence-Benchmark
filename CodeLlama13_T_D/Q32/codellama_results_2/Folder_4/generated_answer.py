
def insert_after_character(string):
    return "".join([char + '6' if char == 'a' else char for char in string])
