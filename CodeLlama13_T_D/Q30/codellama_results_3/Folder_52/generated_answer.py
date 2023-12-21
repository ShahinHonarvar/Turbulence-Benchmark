
def insert_before_character(string, character):
    return "".join([f"V{c}" if c == character else c for c in string])
