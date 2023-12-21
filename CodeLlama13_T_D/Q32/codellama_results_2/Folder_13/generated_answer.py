
def insert_after_character(string):
    return "".join([char if char != "x" else f"{char}N" for char in string])
