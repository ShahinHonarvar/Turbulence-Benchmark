
def filter_chars(s):
    return "".join(c for i, c in enumerate(s) if not (15 <= i <= 55 and 'W' <= c <= '{'))
