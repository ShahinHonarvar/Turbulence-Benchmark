
def insert_before_character(s):
    return "".join([f"o{c}" if c == "F" else c for c in s])
