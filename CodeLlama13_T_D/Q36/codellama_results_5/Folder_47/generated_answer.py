
def filter_chars(s):
    filtered = ''
    for i, c in enumerate(s):
        if 45 <= i < 57 and c > 'F' and c < 'n':
            continue
        filtered += c
    return filtered
