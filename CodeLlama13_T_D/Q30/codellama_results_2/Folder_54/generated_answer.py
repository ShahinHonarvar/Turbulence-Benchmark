
def insert_before_character(string, char):
    return "".join([f"{char}f" if c == char else c for c in string])
