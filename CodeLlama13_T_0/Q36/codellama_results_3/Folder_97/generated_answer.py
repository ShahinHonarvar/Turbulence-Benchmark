
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 309 or i > 591:
            new_str += char
        elif char > "S" and char < "m":
            new_str += char
    return new_str
