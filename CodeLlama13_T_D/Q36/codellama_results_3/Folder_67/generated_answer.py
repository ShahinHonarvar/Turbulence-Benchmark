
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if (i > 18 and i < 31) and (char > "H" and char < "|"):
            continue
        else:
            new_str += char
    return new_str
