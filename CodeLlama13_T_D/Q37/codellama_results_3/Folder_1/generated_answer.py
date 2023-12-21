
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if 41 <= i <= 79 and 'f' <= char <= '|':
            continue
        else:
            new_str += char
    return new_str
