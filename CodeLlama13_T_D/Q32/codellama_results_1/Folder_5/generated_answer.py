
def insert_after_character(string):
    return "".join(char if char != "G" else "cG" for char in string)
