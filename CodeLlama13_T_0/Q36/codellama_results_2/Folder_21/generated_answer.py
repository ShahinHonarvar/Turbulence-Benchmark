
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 219 or i > 403:
            new_str += char
        elif char > "*" and char < "7":
            new_str += char
    return new_str
