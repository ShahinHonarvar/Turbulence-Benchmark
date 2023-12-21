
def insert_after_character(string):
    return "".join([char if char != "i" else f"{char}0" for char in string])
