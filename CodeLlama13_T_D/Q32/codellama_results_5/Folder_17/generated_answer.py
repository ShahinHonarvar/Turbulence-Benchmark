
def insert_after_character(string):
    return "".join([char if char != "I" else "Q" + char for char in string])
