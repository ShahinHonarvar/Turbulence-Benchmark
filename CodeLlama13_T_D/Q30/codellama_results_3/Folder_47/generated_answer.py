
def insert_before_character(string):
    return "".join("f" + c if c == 'E' else c for c in string)
