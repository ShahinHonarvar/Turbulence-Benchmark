
def insert_after_character(string):
    return "".join([char + "X" if char == " " else char for char in string])
