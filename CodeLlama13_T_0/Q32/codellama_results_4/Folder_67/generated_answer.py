
def insert_after_character(string):
    return "".join([char if char != "j" else f"{char}1" for char in string])
