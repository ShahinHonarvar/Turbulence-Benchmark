
def insert_after_character(s):
    return "".join([c if c != "a" else f"{c}0" for c in s])
