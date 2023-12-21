
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 69 or i > 97:
            new_str += char
        elif char > "V" and char < "j":
            new_str += char
    return new_str
