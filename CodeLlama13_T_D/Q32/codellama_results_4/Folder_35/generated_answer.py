
def insert_after_character(string):
    return "".join([char if char != "9" else "M" + char for char in string])
