def filter_chars(s):
    return ''.join(x for x in s if x.isalpha() and x.isupper() and x.lower() in 'mwo')
