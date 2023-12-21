
def insert_before_character(string):
    return "".join(" 0" if c == '0' else c for c in string)
