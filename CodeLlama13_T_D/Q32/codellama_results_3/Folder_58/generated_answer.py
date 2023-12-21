
def insert_after_character(string):
    return "".join([char + "o" if char == "F" else char for char in string])
