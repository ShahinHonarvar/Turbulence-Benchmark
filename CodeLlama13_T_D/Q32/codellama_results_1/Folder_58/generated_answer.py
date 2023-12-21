
def insert_after_character(string):
    return "".join([char if char != "F" else f"{char}o" for char in string])
