
def insert_before_character(string):
    return "".join([f"H{c}" if c == "0" else c for c in string])
