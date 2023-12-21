
def filter_chars(x):
    for i, c in enumerate(x):
        if 515 <= i <= 538 and '+' <= c <= '}':
            x = x.replace(c, "")
    return x
