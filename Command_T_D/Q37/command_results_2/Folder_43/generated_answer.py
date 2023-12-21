def filter_chars(s):
    return s.translate(str.maketrans(range(15, 55 + 1), range(15, 55 + 1)))
