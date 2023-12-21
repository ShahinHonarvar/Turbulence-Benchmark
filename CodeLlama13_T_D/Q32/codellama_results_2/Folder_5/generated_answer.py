
def insert_after_character(s):
    return "".join([char + "G" if char == "c" else char for char in s])
