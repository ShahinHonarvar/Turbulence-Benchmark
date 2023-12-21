
def insert_after_character(string, char):
    return "".join([char + "t" if c == "a" else c for c in string])
