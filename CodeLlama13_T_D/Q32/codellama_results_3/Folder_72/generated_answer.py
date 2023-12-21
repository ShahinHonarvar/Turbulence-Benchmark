
def insert_after_character(string):
    return "".join([char if char != "d" else f"{char}O" for char in string])
