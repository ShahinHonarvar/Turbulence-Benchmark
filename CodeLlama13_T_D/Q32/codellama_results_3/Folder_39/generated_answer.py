
def insert_after_character(string):
    return "".join([char if char != "Q" else "mQ" for char in string])
