
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 154 or i > 222:
            new_str += char
        elif char < "A" or char > "f":
            new_str += char
        else:
            new_str += char
    return new_str
