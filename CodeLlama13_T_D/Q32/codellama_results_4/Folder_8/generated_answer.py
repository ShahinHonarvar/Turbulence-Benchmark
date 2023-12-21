
def insert_after_character(s):
    return "".join([c if c != "E" else f"{c}T" for c in s])
