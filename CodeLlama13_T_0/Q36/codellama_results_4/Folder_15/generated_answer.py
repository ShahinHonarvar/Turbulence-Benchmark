
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if 2 <= i < 7 and char > "h" and char < "k":
            new_str += char
    return new_str
