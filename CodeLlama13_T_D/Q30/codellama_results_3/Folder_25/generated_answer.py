
def insert_before_character(string):
    return "".join("W" + c if c == 'e' else c for c in string)
