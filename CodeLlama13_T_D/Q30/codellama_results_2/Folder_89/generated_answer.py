
def insert_before_character(string):
    return "".join([char if char != " " else f"W{char}" for char in string])
