
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 587 or i > 648:
            new_str += char
        elif char > "," and char < "c":
            continue
        else:
            new_str += char
    return new_str
