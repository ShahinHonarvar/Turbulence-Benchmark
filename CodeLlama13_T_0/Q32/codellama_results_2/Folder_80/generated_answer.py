
def insert_after_character(string):
    return "".join([char if char != " " else f"X{char}" for char in string])
