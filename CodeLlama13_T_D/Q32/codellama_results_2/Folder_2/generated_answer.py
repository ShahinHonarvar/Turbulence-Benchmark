
def insert_after_character(string):
    return "".join([c + ("Z" if c == "C" else "") for c in string])
