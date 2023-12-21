
def insert_before_character(string, char):
    return "".join([char + "5" if c == " " else c for c in string])
