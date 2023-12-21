
def insert_after_character(string):
    return "".join([char if char != "O" else "Q" + char for char in string])
