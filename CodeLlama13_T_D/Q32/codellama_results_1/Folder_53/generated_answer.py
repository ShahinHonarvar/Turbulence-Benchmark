
def insert_after_character(string):
    return "".join([char if char != "i" else f"{char}I" for char in string])
