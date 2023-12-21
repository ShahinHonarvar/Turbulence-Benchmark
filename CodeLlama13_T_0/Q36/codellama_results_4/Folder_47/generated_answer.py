
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 45 or i > 57:
            new_str += char
        elif char > "F" and char < "n":
            new_str += char
    return new_str
