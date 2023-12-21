
def insert_before_character(s):
    return "".join([f"o{c}" if c == " " else c for c in s])
