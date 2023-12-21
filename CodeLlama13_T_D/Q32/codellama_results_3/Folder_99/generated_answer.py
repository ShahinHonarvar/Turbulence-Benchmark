
def insert_after_character(string):
    return "".join([char if char != "a" else "W" + char for char in string])
