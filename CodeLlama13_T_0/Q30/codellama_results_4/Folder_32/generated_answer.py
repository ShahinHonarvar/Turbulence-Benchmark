
def insert_before_character(string):
    return "".join([char if char != "u" else f"u{char}" for char in string])
