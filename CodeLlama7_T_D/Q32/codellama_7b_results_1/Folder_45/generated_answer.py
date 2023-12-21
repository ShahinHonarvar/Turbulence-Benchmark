
def insert_after_character(string):
    return "".join([char + "O" if char == "O" else char for char in string])
