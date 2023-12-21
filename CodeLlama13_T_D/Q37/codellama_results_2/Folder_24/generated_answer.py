
def filter_chars(s):
    new_str = ''
    for i, c in enumerate(s):
        if i >= 36 and i <= 79 and ord(c) >= ord('2') and ord(c) <= ord('s'):
            new_str += c
    return new_str
