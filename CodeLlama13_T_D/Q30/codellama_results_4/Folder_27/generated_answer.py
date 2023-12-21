
def insert_before_character(string):
    return "".join([char if char != "N" else f"j{char}" for char in string])
