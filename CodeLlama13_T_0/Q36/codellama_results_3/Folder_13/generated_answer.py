
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if i < 323 or i > 526:
            new_str += char
        elif char > ")" and char < "O":
            continue
        else:
            new_str += char
    return new_str
