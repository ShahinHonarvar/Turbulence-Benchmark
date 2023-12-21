
def insert_after_character(string):
    return "".join([char if char != "Z" else f"{char}C" for char in string])
