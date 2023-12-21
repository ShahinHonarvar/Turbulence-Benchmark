
def insert_after_character(string):
    return "".join([char + "o" if char == " " else char for char in string])
