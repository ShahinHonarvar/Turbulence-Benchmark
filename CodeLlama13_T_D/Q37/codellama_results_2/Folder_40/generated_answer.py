
def filter_chars(s):
    return ''.join([c for c in s if (0 <= ord(c) - ord('*') < 17 and c != '*' and c != 's')])
