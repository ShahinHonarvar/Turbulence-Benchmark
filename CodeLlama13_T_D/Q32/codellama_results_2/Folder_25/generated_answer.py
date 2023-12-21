
def insert_after_character(s):
    return "".join([f"{c}W" if c == 'e' else c for c in s])
