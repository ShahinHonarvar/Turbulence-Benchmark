
def insert_before_character(s):
    return "".join("G" + c if c == 'c' else c for c in s)
