
def insert_after_character(string):
    return "".join([c if c != "F" else f"{c}U" for c in string])
