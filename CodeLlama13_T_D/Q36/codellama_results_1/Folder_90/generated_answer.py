
def filter_chars(s):
    return ''.join([c for c in s if not (344 < ord(c) < 874 or c > 'f' and c < '~')])
