
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if 31 < ord(char) < 73 and char not in "Mj":
            new_str += char
    return new_str
