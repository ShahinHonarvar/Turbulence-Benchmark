def filter_chars(s):
    return ''.join(c for c in s if not (c.isalpha() and c.isupper() and 32 <= ord(c) <= 61))
