def filter_chars(str1):
    return "".join(x for x in str1 if x not in list(range(155, 403)) + list(range(91, 123)))
