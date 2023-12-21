def filter_chars(s):
    return s.replace(list(range(54, 62, 1)), ")\0\1\2\3\4\5\6\7\8")
