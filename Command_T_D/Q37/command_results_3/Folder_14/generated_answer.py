def filter_chars(s):
    return ''.join(c for c in s if c.isalpha() and ord(c) in range(ord('A') + 35, ord('b') + 98))
