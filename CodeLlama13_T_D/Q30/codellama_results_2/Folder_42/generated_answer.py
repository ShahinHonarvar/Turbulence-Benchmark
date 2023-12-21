
def insert_before_character(string):
    return "".join([f"j{c}" if c == "O" else c for c in string])
