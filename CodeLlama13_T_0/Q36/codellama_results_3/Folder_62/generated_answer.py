
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if 63 < ord(char) < 89 and char != "*":
            continue
        else:
            new_str += char
    return new_str
