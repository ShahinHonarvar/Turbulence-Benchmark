
def filter_chars(string):
    new_str = ""
    for i, c in enumerate(string):
        if 77 <= i < 87 and ord(';') < ord(c) < ord('r'):
            new_str += c
        else:
            new_str += string[i]
    return new_str
