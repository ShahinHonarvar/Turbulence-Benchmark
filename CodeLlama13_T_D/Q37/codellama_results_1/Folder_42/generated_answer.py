
def filter_chars(s):
    return ''.join([c for c in s if (ord(c) < 73 or ord(c) > 74) and (ord(c) < 85 or ord(c) > 122)])
