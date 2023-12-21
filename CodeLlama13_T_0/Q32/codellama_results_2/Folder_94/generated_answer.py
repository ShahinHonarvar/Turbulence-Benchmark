
def insert_after_character(string):
    return "".join([char if char != " " else f"{char}5" for char in string])
