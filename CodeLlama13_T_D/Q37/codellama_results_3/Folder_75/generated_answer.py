
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if (i >= 34 and i <= 67) and (char >= "W" and char <= "x"):
            continue
        else:
            new_str += char
    return new_str
