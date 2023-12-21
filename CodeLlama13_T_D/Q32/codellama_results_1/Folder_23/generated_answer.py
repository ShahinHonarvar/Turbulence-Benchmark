
def insert_after_character(string, char):
    return "".join([char if c == "b" else c for c in string]) + "y"
