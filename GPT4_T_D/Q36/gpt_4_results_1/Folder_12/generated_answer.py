
def filter_chars(s):
    filtered_chars = [ch for i, ch in enumerate(s) if (i > 32 and i < 84) and (ch <= 'm' or ch >= 'w')]
    return ''.join(filtered_chars)
