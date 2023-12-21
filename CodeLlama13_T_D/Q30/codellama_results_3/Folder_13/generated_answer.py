
def insert_before_character(s):
    return "".join("N" + c if c == "x" else c for c in s)
