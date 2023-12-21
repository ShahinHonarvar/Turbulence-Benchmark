
def insert_after_character(string):
    return "".join([char if char != "W" else f"{char}e" for char in string])
