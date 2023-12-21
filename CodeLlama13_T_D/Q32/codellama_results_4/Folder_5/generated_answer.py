
def insert_after_character(string):
    return "".join([char + "G" if char == "c" else char for char in string])
