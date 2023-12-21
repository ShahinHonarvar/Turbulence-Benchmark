
def insert_before_character(string):
    return "".join([char if char != "N" else "z" + char for char in string])
