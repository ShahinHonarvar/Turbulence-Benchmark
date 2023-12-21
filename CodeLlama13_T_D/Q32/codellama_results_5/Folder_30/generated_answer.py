
def insert_after_character(string):
    return "".join([char if char != "4" else "4F" for char in string])
