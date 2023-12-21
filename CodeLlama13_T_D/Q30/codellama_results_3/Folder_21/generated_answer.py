
def insert_before_character(string):
    return "".join([f"K{c}" if c == " " else c for c in string])
