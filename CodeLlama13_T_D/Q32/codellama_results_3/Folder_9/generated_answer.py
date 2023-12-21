
def insert_after_character(string):
    return "".join([char if char != "e" else f"{char}E" for char in string])
