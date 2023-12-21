
def insert_after_character(s):
    return "".join([c + "u" if c == "X" else c for c in s])
