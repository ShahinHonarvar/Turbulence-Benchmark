
def insert_before_character(string, char):
    return "".join([f"{char}{s}" if s == char else s for s in string])
