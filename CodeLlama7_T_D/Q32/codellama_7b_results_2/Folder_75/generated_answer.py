
def insert_after_character(s):
    return "".join([c if c != "U" else "Uq" for c in s])
