
def filter_chars(string):
    new_str = ""
    for char in string:
        if char not in "UL":
            new_str += char
    return new_str
