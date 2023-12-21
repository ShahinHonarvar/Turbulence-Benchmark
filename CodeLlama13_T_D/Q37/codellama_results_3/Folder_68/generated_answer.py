
def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if i < 7 or i > 9:
            result += c
        elif '6' <= c and c <= 'w':
            continue
        else:
            result += c
    return result
