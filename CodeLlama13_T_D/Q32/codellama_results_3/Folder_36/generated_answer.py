
def insert_after_character(string):
    return "".join([char if char != "A" else f"A{char}" for char in string])
