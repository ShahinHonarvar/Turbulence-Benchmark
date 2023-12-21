
def filter_chars(s):
    return ''.join([c for c in s if 86 <= ord(c) <= 92 and '!' <= c <= 's'])
