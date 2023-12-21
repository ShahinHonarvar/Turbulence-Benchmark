def filter_chars(s):
    return ''.join(x for x in s if x.isalpha() and x.isupper() and x.isdigit() and x.isalnum() and x in range('6', '_', 1))
