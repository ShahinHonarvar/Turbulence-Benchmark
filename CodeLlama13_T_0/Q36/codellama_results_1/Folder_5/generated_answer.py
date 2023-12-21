
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 55 or i > 66:
            new_str += char
        elif char > "f" and char < "|":
            continue
        else:
            new_str += char
    return new_str
