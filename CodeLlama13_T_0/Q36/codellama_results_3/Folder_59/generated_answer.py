
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 3 or i > 8:
            new_str += char
        elif char > "?" and char < "k":
            new_str += char
    return new_str
