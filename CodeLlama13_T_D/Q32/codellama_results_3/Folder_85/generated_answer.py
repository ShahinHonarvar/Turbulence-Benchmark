
def insert_after_character(string):
    return "".join([char + "a" if char == "o" else char for char in string])
