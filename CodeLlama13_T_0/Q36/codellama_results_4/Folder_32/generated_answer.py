
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 40 or i > 63:
            new_str += char
        elif char > "7" and char < "H":
            new_str += char
    return new_str
