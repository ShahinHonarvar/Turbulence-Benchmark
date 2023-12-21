
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if 23 <= i < 83 and 'f' < char < 'o':
            continue
        else:
            new_str += char
    return new_str
