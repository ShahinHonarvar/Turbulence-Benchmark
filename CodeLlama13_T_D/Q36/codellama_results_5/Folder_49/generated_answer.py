
def filter_chars(s):
    chars = list(s)
    for i in range(46, 91):
        if ord('D') < i < ord('H'):
            chars = [c for c in chars if c != chr(i)]
    return ''.join(chars)
