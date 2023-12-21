
def insert_after_character(string):
    return "".join([char + "S" if char == '2' else char for char in string])
