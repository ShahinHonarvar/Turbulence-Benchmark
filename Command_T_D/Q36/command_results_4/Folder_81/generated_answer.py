def filter_chars(s):
    return s.translate(str.maketrans("5BCHJKMPTUVWXX", ""))
