
def insert_before_character(s):
    return "".join([c if c != "f" else f"{c}M" for c in s])
