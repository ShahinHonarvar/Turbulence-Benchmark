
def insert_before_character(string):
    return "".join([char if char != "R" else f"{char}5" for char in string])
