
def insert_after_character(string):
    return "".join([char if char != "i" else "0" + char for char in string])
