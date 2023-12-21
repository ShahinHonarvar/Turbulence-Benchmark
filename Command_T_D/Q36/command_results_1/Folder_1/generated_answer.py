def filter_chars(s):
    return '#' + '#'.join(c for c in s[69:-1] if c in 'KLMNPQRSTUVWXX') + '#'
