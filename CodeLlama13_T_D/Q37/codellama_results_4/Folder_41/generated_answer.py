
def filter_chars(s):
    new_str = ""
    for i, c in enumerate(s):
        if i < 26 or i > 64:
            continue
        elif ord('V') <= ord(c) <= ord('o'):
            continue
        else:
            new_str += c
    return new_str
