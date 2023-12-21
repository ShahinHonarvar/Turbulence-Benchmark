def filter_chars(s):
    return ''.join(c for c in s if c.isalpha() and 0 <= ord(c) - ord('H') <= 5)
