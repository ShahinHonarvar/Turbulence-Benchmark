
def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if 31 < ord(c) < 74 and s[i] != 'M' and s[i] != 'j':
            result += c
    return result
