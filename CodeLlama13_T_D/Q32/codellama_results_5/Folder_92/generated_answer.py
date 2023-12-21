
def insert_after_character(string, char):
    return "".join(char + char if c == char else c for c in string)
