
def insert_after_character(string):
    return "".join([char + "H" if char == " " else char for char in string])
