
def insert_before_character(string, char):
    return "".join([f"u{char}" if c == 'X' else c for c in string])
