
def insert_before_character(s):
    return "".join([f"{c}e" if c == "e" else c for c in s])
