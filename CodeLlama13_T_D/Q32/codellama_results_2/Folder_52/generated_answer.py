
def insert_after_character(string):
    return "".join([char + "V" if char == "T" else char for char in string])
