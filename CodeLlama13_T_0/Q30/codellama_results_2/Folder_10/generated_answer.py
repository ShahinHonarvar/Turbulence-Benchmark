
def insert_before_character(string):
    return "".join([char if char != "j" else "v" + char for char in string])
