
def insert_after_character(string):
    return "".join([char if char != "W" else f"{char}6" for char in string])
