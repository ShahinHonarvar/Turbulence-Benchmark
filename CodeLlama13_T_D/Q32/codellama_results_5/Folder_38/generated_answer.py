
def insert_after_character(string):
    return "".join([char + ("6" if char == "X" else "") for char in string])
