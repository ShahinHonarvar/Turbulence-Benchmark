
def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if 36 <= ord(c) <= 79 and '2' <= c <= 's':
            continue
        else:
            result += c
    return result
