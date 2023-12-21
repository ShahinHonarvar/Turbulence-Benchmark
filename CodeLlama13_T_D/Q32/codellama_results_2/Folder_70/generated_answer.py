
def insert_after_character(string):
    return "".join([char if char != "P" else f"{char}V" for char in string])
