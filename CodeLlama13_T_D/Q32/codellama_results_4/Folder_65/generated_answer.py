
def insert_after_character(string):
    return "".join([char if char != "9" else f"6{char}" for char in string])
