
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 3 or i > 9:
            new_str += char
        elif char > "*" and char < "E":
            new_str += char
    return new_str
