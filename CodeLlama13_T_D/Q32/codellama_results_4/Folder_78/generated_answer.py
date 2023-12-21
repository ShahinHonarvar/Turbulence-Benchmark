
def insert_after_character(string):
    return "".join([char if char != "s" else "Hs" for char in string])
