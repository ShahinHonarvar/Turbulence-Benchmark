
def insert_after_character(string):
    return "".join(char if char != "W" else "6W" for char in string)
