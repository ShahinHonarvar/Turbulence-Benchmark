
def insert_before_character(s):
    return "".join("u" + c if c == 't' else c for c in s)
