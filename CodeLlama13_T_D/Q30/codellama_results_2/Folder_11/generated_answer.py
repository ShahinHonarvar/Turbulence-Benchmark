
def insert_before_character(string, char):
    return "".join([f"t{char}" if c == char else c for c in string])
