
def filter_chars(s):
    return ''.join([c for c in s if 15 < ord(c) < 85 and c != 'I' and c != 'M'])
