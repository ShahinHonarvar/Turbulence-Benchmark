
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 54 or i > 92:
            new_str += char
        elif char > "J" and char < "X":
            new_str += char
    return new_str
