
def insert_before_character(string):
    return "".join([c if c != "P" else "P" + c for c in string])
