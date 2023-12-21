
def insert_before_character(string):
    return "".join([char if char != 'F' else f"F{char}" for char in string])
