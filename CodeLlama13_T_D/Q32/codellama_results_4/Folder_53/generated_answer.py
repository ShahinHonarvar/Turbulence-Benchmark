
def insert_after_character(string):
    return "".join([char if char != "I" else "iI" for char in string])
