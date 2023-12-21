
def filter_chars(s):
    chars = []
    for c in s:
        if ord('-') <= ord(c) <= ord('n'):
            chars.append(c)
    return ''.join(chars)
