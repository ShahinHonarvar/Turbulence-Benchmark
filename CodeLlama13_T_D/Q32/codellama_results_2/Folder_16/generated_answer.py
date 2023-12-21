
def insert_after_character(string):
    return "".join([char + "n" if char == "w" else char for char in string])
