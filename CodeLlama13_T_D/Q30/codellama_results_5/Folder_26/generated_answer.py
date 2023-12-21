
def insert_before_character(s, c):
    return "".join([f"w{c}" if c == "r" else c for c in s])
