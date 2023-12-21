
def insert_after_character(string):
    return "".join([char if char != "b" else "by" for char in string])
