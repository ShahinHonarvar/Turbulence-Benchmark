def filter_chars(s):
    return "".join(c for i, c in enumerate(s) if i < 23 or i > 89 or c in 'w{')
