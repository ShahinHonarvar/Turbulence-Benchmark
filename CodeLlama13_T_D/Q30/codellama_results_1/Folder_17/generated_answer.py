
def insert_before_character(string, character):
    return "".join([char if char != 'Q' else f"I{char}" for char in string])
