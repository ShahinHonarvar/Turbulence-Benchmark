
def insert_after_character(string):
    return "".join([char if char != "w" else f"{char}n" for char in string])
