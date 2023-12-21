
def insert_after_character(s):
    return "".join([c if c != "T" else f"{c}V" for c in s])
