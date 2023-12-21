
def insert_after_character(string):
    return "".join([char + "4" if char == "0" else char for char in string])
