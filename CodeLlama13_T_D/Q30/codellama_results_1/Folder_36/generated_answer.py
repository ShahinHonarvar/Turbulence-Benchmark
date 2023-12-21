
def insert_before_character(s, c):
    return "".join([f"H{c}" if c == 'A' else c for c in s])
