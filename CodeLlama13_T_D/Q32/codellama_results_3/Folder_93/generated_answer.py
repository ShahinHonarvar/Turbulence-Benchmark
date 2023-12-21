
def insert_after_character(string):
    return "".join([char + ("4" if char == "Y" else "") for char in string])
