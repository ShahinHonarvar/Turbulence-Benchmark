
def insert_after_character(string):
    return "".join([char if char != "h" else f"{char}h" for char in string])
