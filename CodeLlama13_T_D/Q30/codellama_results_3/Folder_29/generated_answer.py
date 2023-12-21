
def insert_before_character(string, char):
    return "".join([c + char if c == char else c for c in string])
