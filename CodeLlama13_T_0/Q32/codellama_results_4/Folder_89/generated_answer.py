
def insert_after_character(string):
    return "".join([char if char != " " else f"{char}W" for char in string])
