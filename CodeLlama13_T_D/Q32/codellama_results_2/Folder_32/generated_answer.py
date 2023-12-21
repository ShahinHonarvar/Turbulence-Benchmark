
def insert_after_character(string):
    return "".join([f"u{c}" if c == "F" else c for c in string])
