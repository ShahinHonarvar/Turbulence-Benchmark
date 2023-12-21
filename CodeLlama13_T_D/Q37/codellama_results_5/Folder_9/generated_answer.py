
def filter_chars(string):
    result = ""
    for i, c in enumerate(string):
        if i >= 38 and i <= 99 and 'A' <= c <= 'Q':
            continue
        result += c
    return result
