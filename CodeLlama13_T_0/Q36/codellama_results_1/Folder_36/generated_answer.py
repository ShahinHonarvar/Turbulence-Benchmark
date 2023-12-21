
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 283 or i > 484:
            new_str += char
        elif char > "l" and char < "t":
            continue
        else:
            new_str += char
    return new_str
