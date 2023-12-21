
def insert_before_character(string):
    return "".join([c if c != "e" else "E" + c for c in string])
