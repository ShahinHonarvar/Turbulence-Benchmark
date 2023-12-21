
def insert_before_character(string):
    return "".join("S" + c if c == "2" else c for c in string)
