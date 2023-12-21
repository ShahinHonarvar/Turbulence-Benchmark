
def insert_after_character(string):
    return "".join([char if char != "G" else "Gc" for char in string])
