
def insert_before_character(s, c):
    return "".join([f"j{c}" if x == "O" else x for x in s])
