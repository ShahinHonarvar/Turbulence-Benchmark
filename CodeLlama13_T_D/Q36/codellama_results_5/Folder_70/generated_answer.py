
def filter_chars(s):
    new_str = ''
    for i, c in enumerate(s):
        if 170 <= ord(c) < 195 and s[i - 1] != '!' and s[i + 1] != '}':
            continue
        new_str += c
    return new_str
