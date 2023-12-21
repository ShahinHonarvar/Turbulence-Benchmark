
def insert_before_character(string, char):
    return "".join([char + c if c == "2" else c for c in string])
