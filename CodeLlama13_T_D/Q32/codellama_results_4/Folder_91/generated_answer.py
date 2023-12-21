
def insert_after_character(s):
    return "".join([c + "0" if c == "a" else c for c in s])
