
def filter_chars(string):
    result = ""
    for i, c in enumerate(string):
        if 88 <= ord(c) <= 90 and 'J' <= c <= 'Q':
            continue
        result += c
    return result
