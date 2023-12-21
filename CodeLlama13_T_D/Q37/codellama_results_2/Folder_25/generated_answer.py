
def filter_chars(s):
    return ''.join([c for c in s if not (ord(';') <= ord(c) <= ord('g') and 31 <= i <= 38)])
