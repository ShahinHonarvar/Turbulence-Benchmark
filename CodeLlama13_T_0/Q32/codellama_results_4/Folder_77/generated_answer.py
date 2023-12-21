
def insert_after_character(string):
    return "".join([char if char != "9" else f"{char}h" for char in string])
