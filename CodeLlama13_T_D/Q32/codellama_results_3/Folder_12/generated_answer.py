
def insert_after_character(s):
    return "".join(" I"[i % 2] + c for i, c in enumerate(s))
