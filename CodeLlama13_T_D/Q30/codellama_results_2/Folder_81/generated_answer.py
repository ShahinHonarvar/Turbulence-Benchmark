
def insert_before_character(string):
    return "".join("A" + c if c == "A" else c for c in string)
