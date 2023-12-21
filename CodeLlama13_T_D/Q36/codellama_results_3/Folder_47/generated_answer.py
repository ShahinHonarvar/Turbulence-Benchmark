
def filter_chars(string):
    result = ''
    for i, c in enumerate(string):
        if 45 < ord(c) < 57 and c > 'F' and c < 'n':
            continue
        else:
            result += c
    return result
