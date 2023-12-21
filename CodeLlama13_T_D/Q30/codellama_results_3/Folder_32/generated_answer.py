
def insert_before_character(s):
    return "".join([f"u{c}" if c == 'F' else c for c in s])
