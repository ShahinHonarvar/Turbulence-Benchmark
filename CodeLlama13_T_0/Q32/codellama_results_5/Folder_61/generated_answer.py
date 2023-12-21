
def insert_after_character(string):
    return "".join([char if char != "e" else f"{char}0" for char in string])
