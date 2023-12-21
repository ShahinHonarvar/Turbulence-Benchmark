
def insert_after_character(string):
    return "".join([char + "N" if char == 'm' else char for char in string])
