
def insert_after_character(string):
    return "".join([char + "w" if char == "s" else char for char in string])
