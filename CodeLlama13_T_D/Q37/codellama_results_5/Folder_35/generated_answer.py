
def filter_chars(s):
    return "".join([c for c in s if not (155 <= ord(c) <= 403 and '(' <= c <= ']')])
