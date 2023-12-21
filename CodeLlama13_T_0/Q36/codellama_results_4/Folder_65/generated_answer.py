
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 58 or i > 82:
            new_str += char
        elif char > "F" and char < "O":
            continue
        else:
            new_str += char
    return new_str
