
def filter_chars(s):
    return ''.join([c for c in s if (ord(c) < 503 or ord(c) > 753 or ord(c) < 9 or ord(c) > 122)])
