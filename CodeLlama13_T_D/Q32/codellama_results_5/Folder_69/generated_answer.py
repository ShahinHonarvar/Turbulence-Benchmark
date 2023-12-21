
def insert_after_character(s, c):
    return "".join([char if char != c else f"{c}{c}" for char in s])
