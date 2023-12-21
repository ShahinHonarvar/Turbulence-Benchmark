
def filter_chars(string):
    chars = list(string)
    for i in range(12, 26):
        if 'P' <= chars[i] <= 'x':
            chars = [c for c in chars if c != chars[i]]
    return ''.join(chars)
