
def insert_before_character(string):
    return "".join([f"0{c}" if c == "i" else c for c in string])
