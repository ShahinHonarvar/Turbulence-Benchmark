
def insert_after_character(s):
    return "".join([char + "S" if char == "2" else char for char in s])
