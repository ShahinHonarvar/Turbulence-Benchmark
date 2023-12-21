
def insert_before_character(s):
    return "".join("W" + c if c == "e" else c for c in s)
