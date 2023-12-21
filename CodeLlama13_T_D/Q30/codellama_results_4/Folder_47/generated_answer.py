
def insert_before_character(s):
    return "".join([f"{c}f" if c == "E" else c for c in s])
