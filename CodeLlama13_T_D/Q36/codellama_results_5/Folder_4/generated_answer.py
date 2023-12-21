
def filter_chars(s):
    chars = list(s)
    for i in range(42, 67):
        if chars[i].isalpha() and '6' < chars[i] < 'g':
            chars.remove(chars[i])
    return ''.join(chars)
