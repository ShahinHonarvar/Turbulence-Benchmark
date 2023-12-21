
def filter_chars(string):
    new_str = ""
    for i, c in enumerate(string):
        if i < 23 or i > 45:
            new_str += c
        elif ord(c) > ord('3') and ord(c) < ord('I'):
            new_str += c
    return new_str
