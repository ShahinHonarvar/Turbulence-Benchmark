
def insert_after_character(s):
    return "".join([char if char != "E" else f"{char}f" for char in s])
