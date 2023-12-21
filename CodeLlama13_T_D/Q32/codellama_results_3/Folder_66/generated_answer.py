
def insert_after_character(string):
    return "".join([char if char != "k" else f"{char}k" for char in string])
