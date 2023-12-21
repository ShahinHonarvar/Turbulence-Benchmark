
def insert_before_character(string, character):
    return "".join([f"{c}{'t' if c == 'a' else ''}" for c in string])
