
def insert_after_character(string):
    return "".join([char if char != 'A' else f"{char}a" for char in string])
