def filter_chars(s):
    return ''.join(c for c in s if c.isalpha() and ord(c) in range(26, 65, 1) and c.lower() in 'vow')
