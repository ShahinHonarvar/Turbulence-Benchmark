
def insert_before_character(string, char):
    return "".join([f"V{char}" if c == char else c for c in string])
