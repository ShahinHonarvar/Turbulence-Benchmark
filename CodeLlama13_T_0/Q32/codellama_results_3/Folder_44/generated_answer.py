
def insert_after_character(string):
    return "".join([char if char != "g" else f"{char}M" for char in string])
