
def insert_before_character(string):
    return "".join([char if char != "S" else f"{char}2" for char in string])
