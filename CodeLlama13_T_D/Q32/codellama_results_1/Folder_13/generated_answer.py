
def insert_after_character(string):
    return "".join([char + "N" if char == "x" else char for char in string])
