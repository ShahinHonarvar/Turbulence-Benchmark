
def insert_after_character(string):
    return "".join(char if char != "T" else f"{char} " for char in string)
