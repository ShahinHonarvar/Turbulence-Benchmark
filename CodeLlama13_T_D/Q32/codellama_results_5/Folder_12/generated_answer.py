
def insert_after_character(s):
    return "".join([char if char != 'I' else f"{char} " for char in s])
