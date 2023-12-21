
def insert_after_character(string):
    return "".join([char + "l" if char == "K" else char for char in string])
