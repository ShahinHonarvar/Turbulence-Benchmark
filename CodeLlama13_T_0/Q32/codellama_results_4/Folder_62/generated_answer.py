
def insert_after_character(string):
    return "".join([char if char != " " else f"{char}o" for char in string])
