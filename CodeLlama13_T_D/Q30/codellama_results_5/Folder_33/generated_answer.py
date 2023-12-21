
def insert_before_character(string):
    return "".join([f"n{c}" if c == "a" else c for c in string])
