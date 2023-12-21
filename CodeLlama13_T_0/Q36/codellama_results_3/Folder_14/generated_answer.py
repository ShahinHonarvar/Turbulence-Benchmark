
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 41 or i > 56:
            new_str += char
        elif char > "Z" and char < "c":
            continue
        else:
            new_str += char
    return new_str
