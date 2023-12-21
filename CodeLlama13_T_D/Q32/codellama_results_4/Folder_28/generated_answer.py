
def insert_after_character(s):
    return "".join([c if c != "1" else f"{c}r" for c in s])
