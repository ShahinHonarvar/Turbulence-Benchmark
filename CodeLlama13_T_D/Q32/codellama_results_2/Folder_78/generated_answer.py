
def insert_after_character(string):
    return "".join([f"{c}s" if c == "H" else c for c in string])
