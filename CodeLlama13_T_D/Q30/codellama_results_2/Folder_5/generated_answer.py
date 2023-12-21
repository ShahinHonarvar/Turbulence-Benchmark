
def insert_before_character(string):
    return "".join([char if char != "c" else "G" + char for char in string])
