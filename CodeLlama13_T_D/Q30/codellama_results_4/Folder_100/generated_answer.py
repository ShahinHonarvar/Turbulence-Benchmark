
def insert_before_character(string, char):
    return "".join("{} {}".format(char, c) if c == '0' else c for c in string)
