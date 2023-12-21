
def insert_after_character(string):
    return "".join([c if c != "F" else f"{c}u" for c in string])
