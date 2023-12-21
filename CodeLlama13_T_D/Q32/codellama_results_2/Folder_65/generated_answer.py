
def insert_after_character(string):
    return "".join([char if char != "6" else "9" + char for char in string])
