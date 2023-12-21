
def insert_after_character(string):
    return "".join([char if char != "M" else f"{char}9" for char in string])
