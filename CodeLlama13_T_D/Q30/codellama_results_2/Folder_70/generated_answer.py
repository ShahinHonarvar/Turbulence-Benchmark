
def insert_before_character(string, char):
    return "".join([f"{char}V" if x == char else x for x in string])
