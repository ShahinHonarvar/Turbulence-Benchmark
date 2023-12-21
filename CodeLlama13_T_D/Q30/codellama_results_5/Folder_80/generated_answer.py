
def insert_before_character(s):
    return "".join("X" + c if c == " " else c for c in s)
