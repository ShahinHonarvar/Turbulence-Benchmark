
def insert_before_character(string):
    return "".join([c if c != "U" else "q" + c for c in string])
