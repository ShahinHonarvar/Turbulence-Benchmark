
def filter_chars(s):
    return ''.join([c for c in s if ord(c) >= 42 and ord(c) <= 92 and ord(c) >= ord('/') and ord(c) <= ord('a')])
