
def filter_chars(s):
    filtered = ''
    for i, char in enumerate(s):
        if 21 <= i <= 43 and '+' <= char <= '8':
            continue
        filtered += char
    return filtered
