
def insert_after_character(string):
    return "".join([char + 'm' if char == 'F' else char for char in string])
