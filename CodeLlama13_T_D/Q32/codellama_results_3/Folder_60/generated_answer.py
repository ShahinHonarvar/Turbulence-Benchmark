
def insert_after_character(string):
    return "".join([char + "P" if char == "C" else char for char in string])
