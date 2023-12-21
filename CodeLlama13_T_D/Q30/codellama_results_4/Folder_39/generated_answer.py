
def insert_before_character(s, char):
    return "".join([f"Q{c}" if c == 'm' else c for c in s])
