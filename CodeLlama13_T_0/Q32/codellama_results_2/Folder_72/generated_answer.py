
def insert_after_character(string):
    return "".join([char if char != "O" else f"{char}d" for char in string])
