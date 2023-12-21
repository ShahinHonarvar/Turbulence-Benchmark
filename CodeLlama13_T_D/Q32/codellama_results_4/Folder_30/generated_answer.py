
def insert_after_character(string):
    return "".join([char + "F" if char == "4" else char for char in string])
