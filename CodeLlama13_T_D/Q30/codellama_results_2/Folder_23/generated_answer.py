
def insert_before_character(s, ch):
    return "".join([c if c != ch else f"y{ch}" for c in s])
