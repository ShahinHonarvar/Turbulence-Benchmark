
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 57 or i > 69:
            new_str += char
        elif char > "(" and char < "W":
            continue
        else:
            new_str += char
    return new_str
