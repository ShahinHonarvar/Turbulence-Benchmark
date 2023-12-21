
def insert_before_character(string):
    return "".join([char if char != "b" else f"y{char}" for char in string])
