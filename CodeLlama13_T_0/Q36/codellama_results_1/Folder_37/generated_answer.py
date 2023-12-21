
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 44 or i > 59:
            new_str += char
        elif char > "/" and char < "6":
            new_str += char
    return new_str
