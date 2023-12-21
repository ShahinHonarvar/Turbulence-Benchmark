
def insert_after_character(string):
    return "".join([char if char != "a" else "aa" for char in string])
