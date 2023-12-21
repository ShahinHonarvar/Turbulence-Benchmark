
def insert_after_character(s):
    return "".join([c + "v" if c == "j" else c for c in s])
