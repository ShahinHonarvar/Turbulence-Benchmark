
def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if 42 <= ord(c) <= 97 and c >= '*' and c <= 'b':
            continue
        result += c
    return result
