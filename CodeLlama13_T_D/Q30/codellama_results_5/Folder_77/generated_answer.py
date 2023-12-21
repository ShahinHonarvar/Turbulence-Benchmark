
def insert_before_character(string):
    return "".join("h" + c if c == "9" else c for c in string)
