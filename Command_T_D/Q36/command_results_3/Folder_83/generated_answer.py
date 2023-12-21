def filter_chars(s):
    return ''.join(x for x in s if not (x.isalpha() and x in 'J<'))
