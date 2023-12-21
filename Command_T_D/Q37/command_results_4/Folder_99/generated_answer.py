def filter_chars(s):
    return ''.join(x for x in s if x.isalpha() and 0 <= ord(x) - ord('T') <= 26)
