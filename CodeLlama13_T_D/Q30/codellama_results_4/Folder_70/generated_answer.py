
def insert_before_character(s):
    return "".join("V" + c if c == "P" else c for c in s)
