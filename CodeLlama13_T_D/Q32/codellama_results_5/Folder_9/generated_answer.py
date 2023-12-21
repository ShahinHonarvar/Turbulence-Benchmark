
def insert_after_character(string):
    return "".join([char if char != "e" else "Ee" for char in string])
