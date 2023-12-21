
def filter_chars(s):
    return ''.join([c for c in s if 124 <= ord(c) <= 854 and ord(c) >= 9 and ord(c) <= 115])
