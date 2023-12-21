
def filter_chars(s):
    return ''.join([c for c in s if (ord(c) < 35 or ord(c) > 89) and c.isalpha()])
