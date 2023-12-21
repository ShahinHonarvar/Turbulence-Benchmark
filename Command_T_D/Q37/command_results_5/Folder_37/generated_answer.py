def filter_chars(s):
    return ''.join(x for x in s if x.isalpha() and x.isupper() and x.index('O') <= x.index('^'))
